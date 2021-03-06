<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:math="http://exslt.org/math" xmlns:exsl="http://exslt.org/common" exclude-result-prefixes="xsl math exsl">
    <xsl:template match="/meal">
        <all>
            <xsl:if test="count(//plate) &gt; 300">
                <xsl:message terminate="yes">You do not have enough money to buy that much food</xsl:message>
            </xsl:if>
            <xsl:variable name="chef-drinks">
                <value>
                    <xsl:value-of select="round(math:random() * 4294967296)" />
                </value>
                <value>
                    <xsl:value-of select="round(math:random() * 4294967296)" />
                </value>
                <value>
                    <xsl:value-of select="round(math:random() * 4294967296)" />
                </value>
                <value>
                    <xsl:value-of select="round(math:random() * 4294967296)" />
                </value>
                <value>
                    <xsl:value-of select="round(math:random() * 4294967296)" />
                </value>
            </xsl:variable>
            <xsl:call-template name="consume-meal">
                <xsl:with-param name="chef-drinks" select="exsl:node-set($chef-drinks)//value" />
                <xsl:with-param name="food-eaten" select="1" />
                <xsl:with-param name="course" select="course[position() = 1]/plate" />
                <xsl:with-param name="drinks" select="state/drinks" />
            </xsl:call-template>
        </all>
    </xsl:template>
    <xsl:template name="consume-meal">
        <xsl:param name="chef-drinks" />
        <xsl:param name="food-eaten" />
        <xsl:param name="course" />
        <xsl:param name="drinks" />
        <xsl:if test="$food-eaten &gt; 30000">
            <xsl:message terminate="yes">You ate too much and died</xsl:message>
        </xsl:if>
        <xsl:if test="count($drinks) &gt; 200">
            <xsl:message terminate="yes">You cannot drink that much</xsl:message>
        </xsl:if>
        <xsl:if test="count($course) &gt; 0">
            <xsl:variable name="c" select="$course[1]" />
            <xsl:variable name="r" select="$course[position()&gt;1]" />
            <xsl:choose>
                <xsl:when test="count($c/宫保鸡丁) = 1">
                    <xsl:message>
                        <chef-drinks>
                            <xsl:copy-of select="$chef-drinks" />
                        </chef-drinks>
                    </xsl:message>
                    <xsl:message>
                        <drinks>
                            <xsl:copy-of select="$drinks" />
                        </drinks>
                    </xsl:message>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="$drinks" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/paella) = 1">
                    <xsl:variable name="newdrinks">
                        <value>
                            <xsl:value-of select="$c/paella + 0" />
                        </value>
                        <xsl:copy-of select="$drinks" />
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="exsl:node-set($newdrinks)//value" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/불고기) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="newdrinks">
                        <value>
                            <xsl:value-of select="$drinks[$arg0 + 2] + 0" />
                        </value>
                        <xsl:copy-of select="$drinks[position() &gt; 1]" />
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="exsl:node-set($newdrinks)//value" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/Борщ) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks[position() &gt; 1 or $chef-drinks[1] != $arg0]" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="$drinks[position() &gt; 1]" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/दाल) = 1">
                    <xsl:if test="count($chef-drinks) = 0">
                        <xsl:copy-of select="document('/flag')" />
                    </xsl:if>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="$drinks" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/ラーメン) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="chefvalue">
                        <value>
                            <xsl:value-of select="$chef-drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="newdrinks">
                        <value>
                            <xsl:value-of select="1 * ($arg0 &gt; $chefvalue)" />
                        </value>
                        <xsl:copy-of select="$drinks[position() &gt; 1]" />
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="exsl:node-set($newdrinks)//value" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/stroopwafels) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="arg1">
                        <value>
                            <xsl:value-of select="$drinks[2] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="newdrinks">
                        <value>
                            <xsl:value-of select="1 * ($arg1 &gt; $arg0)" />
                        </value>
                        <xsl:copy-of select="$drinks[position() &gt; 2]" />
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="exsl:node-set($newdrinks)//value" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/köttbullar) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="arg1">
                        <value>
                            <xsl:value-of select="$drinks[2] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="newdrinks">
                        <xsl:copy-of select="$drinks[($arg1+3) &gt; position() and position() &gt; 2]" />
                        <value>
                            <xsl:value-of select="$arg0" />
                        </value>
                        <xsl:copy-of select="$drinks[position() &gt;= ($arg1 + 3)]" />
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="exsl:node-set($newdrinks)//value" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/γύρος) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="$drinks[position() &gt; 1 and position() != ($arg0 + 2)]" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/rösti) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="arg1">
                        <value>
                            <xsl:value-of select="$drinks[2] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="newdrinks">
                        <value>
                            <xsl:value-of select="$arg0 + $arg1" />
                        </value>
                        <xsl:copy-of select="$drinks[position() &gt; 2]" />
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="exsl:node-set($newdrinks)//value" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/לאַטקעס) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="arg1">
                        <value>
                            <xsl:value-of select="$drinks[2] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="newdrinks">
                        <value>
                            <xsl:value-of select="$arg0 - $arg1" />
                        </value>
                        <xsl:copy-of select="$drinks[position() &gt; 2]" />
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="exsl:node-set($newdrinks)//value" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/poutine) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="arg1">
                        <value>
                            <xsl:value-of select="$drinks[2] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="newdrinks">
                        <value>
                            <xsl:value-of select="$arg0 * $arg1" />
                        </value>
                        <xsl:copy-of select="$drinks[position() &gt; 2]" />
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="exsl:node-set($newdrinks)//value" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/حُمُّص) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="arg1">
                        <value>
                            <xsl:value-of select="$drinks[2] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="newdrinks">
                        <value>
                            <xsl:value-of select="floor($arg0 div $arg1)" />
                        </value>
                        <xsl:copy-of select="$drinks[position() &gt; 2]" />
                    </xsl:variable>
                    <xsl:call-template name="consume-meal">
                        <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                        <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                        <xsl:with-param name="course" select="$r" />
                        <xsl:with-param name="drinks" select="exsl:node-set($newdrinks)//value" />
                    </xsl:call-template>
                </xsl:when>
                <xsl:when test="count($c/æblegrød) = 1">
                    <xsl:variable name="arg0">
                        <value>
                            <xsl:value-of select="$drinks[1] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:variable name="arg1">
                        <value>
                            <xsl:value-of select="$drinks[2] + 0" />
                        </value>
                    </xsl:variable>
                    <xsl:choose>
                        <xsl:when test="$arg0 != 0">
                            <xsl:call-template name="consume-meal">
                                <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                                <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                                <xsl:with-param name="course" select="/meal/course[position() = ($arg1+1)]/plate" />
                                <xsl:with-param name="drinks" select="$drinks[position() &gt; 2]" />
                            </xsl:call-template>
                        </xsl:when>
                        <xsl:otherwise>
                            <xsl:call-template name="consume-meal">
                                <xsl:with-param name="chef-drinks" select="$chef-drinks" />
                                <xsl:with-param name="food-eaten" select="$food-eaten + 1" />
                                <xsl:with-param name="course" select="$r" />
                                <xsl:with-param name="drinks" select="$drinks[position() &gt; 2]" />
                            </xsl:call-template>
                        </xsl:otherwise>
                    </xsl:choose>
                </xsl:when>
            </xsl:choose>
        </xsl:if>
    </xsl:template>
</xsl:stylesheet>