<?php
function _ere2pcre_escape($c) {
    if ($c == "\0") {
        trigger_error('ere2pcre: a literal null byte in the regex', E_USER_ERROR);
    } elseif (strpos('\^$.[]|()?*+{}-/', $c) !== false) {
        return "\\" . $c;
    } else {
        return $c;
    }
}
function _ere2pcre($s, $i) {
    $r = array('');
    $rr = 0;
    $l = strlen($s);
    while ($i < $l) {
        $c = $s[$i];
        if ($c == '(') {
            if ($i + 1 < $l && $s[$i + 1] == ')') {
                $r[$rr].= '()';
                ++$i;
            } else {
                list($t, $ii) = _ere2pcre($s, $i + 1);
                if ($ii >= $l || $s[$ii] != ')') {
                    trigger_error('ere2pcre: "(" does not have a matching ")"', E_USER_ERROR);
                }
                $r[$rr].= '(' . $t . ')';
                $i = $ii;
            }
        } elseif ($c == '[') {
            ++$i;
            $cls = '';
            if ($i < $l && $s[$i] == '^') {
                $cls.= '^';
                ++$i;
            }
            if ($i >= $l) {
                trigger_error('ere2pcre: "[" does not have a matching "]"', E_USER_ERROR);
            }
            $start = true;
            do {
                if ($s[$i] == '[' && $i + 1 < $l && strpos('.=:', $s[$i + 1]) !== false) {
                    $ii = strpos($s, ']', $i);
                    if ($ii === false) {
                        trigger_error('ere2pcre: "[" does not have a matching ' . '"]"', E_USER_ERROR);
                    }
                    $ccls = substr($s, $i + 1, $ii - ($i + 1));
                    $cclsmap = array(':alnum:' => '[:alnum:]', ':alpha:' => '[:alpha:]', ':blank:' => '[:blank:]', ':cntrl:' => '[:cntrl:]', ':digit:' => '\d', ':graph:' => '[:graph:]', ':lower:' => '[:lower:]', ':print:' => '[:print:]', ':punct:' => '[:punct:]', ':space:' => '\013\s', ':upper:' => '[:upper:]', ':xdigit:' => '[:xdigit:]',);
                    if (!isset($cclsmap[$ccls])) {
                        trigger_error('ere2pcre: an invalid or unsupported ' . 'character class [' . $ccls . ']', E_USER_ERROR);
                    }
                    $cls.= $cclsmap[$ccls];
                    $i = $ii + 1;
                } else {
                    $a = $s[$i++];
                    if ($a === '-' && !$start && !($i < $l && $s[$i] == ']')) {
                        trigger_error('ere2pcre: "-" is invalid for the start ' . 'character in the brackets', E_USER_ERROR);
                    }
                    if ($i < $l && $s[$i] === '-') {
                        ++$i;
                        $b = $s[$i++];
                        if ($b == ']') {
                            $cls.= _ere2pcre_escape($a) . '\-';
                            break;
                        } elseif (ord($a) > ord($b)) {
                            trigger_error('ere2pcre: an invalid character ' . 'range "' . $a . '-' . $b . '"', E_USER_ERROR);
                        }
                        $cls.= _ere2pcre_escape($a) . '-' . _ere2pcre_escape($b);
                    } else {
                        $cls.= _ere2pcre_escape($a);
                    }
                }
                $start = false;
            } while ($i < $l && $s[$i] != ']');
            if ($i >= $l) {
                trigger_error('ere2pcre: "[" does not have a matching "]"', E_USER_ERROR);
            }
            $r[$rr].= '[' . $cls . ']';
        } elseif ($c == ')') {
            break;
        } elseif ($c == '*' || $c == '+' || $c == '?') {
            trigger_error('ere2pcre: unescaped metacharacter "' . $c . '"', E_USER_ERROR);
        } elseif ($c == '{') {
            if ($i + 1 < $l && strpos('0123456789', $s[$i + 1]) !== false) {
                $r[$rr].= '\{';
            } else {
                trigger_error('ere2pcre: unescaped metacharacter "' . $c . '"', E_USER_ERROR);
            }
        } elseif ($c == '.') {
            $r[$rr].= $c;
        } elseif ($c == '^' || $c == '$') {
            $r[$rr].= $c;
            ++$i;
            continue;
        } elseif ($c == '|') {
            if ($r[$rr] === '') {
                trigger_error('ere2pcre: empty branch', E_USER_ERROR);
            }
            $r[] = '';
            ++$rr;
            ++$i;
            continue;
        } elseif ($c == "\\") {
            if (++$i >= $l) {
                trigger_error('ere2pcre: an invalid escape sequence at the end', E_USER_ERROR);
            }
            $r[$rr].= _ere2pcre_escape($s[$i]);
        } else {
            $r[$rr].= _ere2pcre_escape($c);
        }
        ++$i;
        if ($i >= $l) break;
        $c = $s[$i];
        if ($c == '*' || $c == '+' || $c == '?') {
            $r[$rr].= $c;
            ++$i;
        } elseif ($c == '{') {
            $ii = strpos($s, '}', $i);
            if ($ii === false) {
                trigger_error('ere2pcre: "{" does not have a matching "}"', E_USER_ERROR);
            }
            $bound = substr($s, $i + 1, $ii - ($i + 1));
            if (!preg_match('/^([0-9]|[1-9][0-9]|1[0-9][0-9]|
                                2[0-4][0-9]|25[0-5])
                               (,([0-9]|[1-9][0-9]|1[0-9][0-9]|
                                  2[0-4][0-9]|25[0-5])?)?$/x', $bound, $m)) {
                trigger_error('ere2pcre: an invalid bound', E_USER_ERROR);
            }
            if (isset($m[3])) {
                if ($m[1] > $m[3]) {
                    trigger_error('ere2pcre: an invalid bound', E_USER_ERROR);
                }
                $r[$rr].= '{' . $m[1] . ',' . $m[3] . '}';
            } elseif (isset($m[2])) {
                $r[$rr].= '{' . $m[1] . ',}';
            } else {
                $r[$rr].= '{' . $m[1] . '}';
            }
            $i = $ii + 1;
        }
    }
    if ($r[$rr] === '') {
        trigger_error('ere2pcre: empty regular expression or branch', E_USER_ERROR);
    }
    return array(implode('|', $r), $i);
}
function ere2pcre($s, $ignorecase) {
    static $cache = array(), $icache = array();
    if ($ignorecase) {
        if (isset($icache[$s])) return $icache[$s];
    } else {
        if (isset($cache[$s])) return $cache[$s];
    }
    list($r, $i) = _ere2pcre($s, 0);
    if ($i != strlen($s)) {
        trigger_error('ere2pcre: unescaped metacharacter ")"', E_USER_ERROR);
    }
    if ($ignorecase) {
        return ($icache[$s] = '/' . $r . '/mi');
    } else {
        return ($cache[$s] = '/' . $r . '/m');
    }
}
if (!function_exists('ereg')) {
    function ereg($r, $s, &$m = null) {
        $r = ere2pcre($r, false);
        if (func_num_args() > 2) {
            return (preg_match($r, $s, $m) ? strlen($m[0]) : false);
        } else {
            return (preg_match($r, $s) ? 1 : false);
        }
    }
}
if (!function_exists('eregi')) {
    function eregi($r, $s, &$m = null) {
        $r = ere2pcre($r, true);
        if (func_num_args() > 2) {
            return (preg_match($r, $s, $m) ? strlen($m[0]) : false);
        } else {
            return (preg_match($r, $s) ? 1 : false);
        }
    }
}
if (!function_exists('ereg_replace')) {
    function ereg_replace($r, $t, $s) {
        return preg_replace(ere2pcre($r, false), $t, $s);
    }
}
if (!function_exists('eregi_replace')) {
    function eregi_replace($r, $t, $s) {
        return preg_replace(ere2pcre($r, true), $t, $s);
    }
}
if (!function_exists('split')) {
    function split($r, $s, $l = - 1) {
        return preg_split(ere2pcre($r, false), $s, ($l == 0 ? 1 : $l));
    }
}
if (!function_exists('spliti')) {
    function spliti($r, $s, $l = - 1) {
        return preg_split(ere2pcre($r, true), $s, ($l == 0 ? 1 : $l));
    }
}
