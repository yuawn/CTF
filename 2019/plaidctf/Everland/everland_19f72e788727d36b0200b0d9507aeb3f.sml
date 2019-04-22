(* 
 *  Setup 
 *
 *    In which we define the realm of terror
 *    Known as... Everland!
 *)

exception CatFlag of string
exception Malformed
exception GameOver of string

type health = int ref
type strength = int ref

type arena = health * strength * health * strength
type move = string * (arena -> ((unit -> unit) * (unit -> unit)))

type item = (string * (int * int * move list))
type bag = item list ref

datatype Enemy =
  Flag
| Nothing
| Opponent of (health * strength * move list * string * Enemy)
| Init of ((Enemy) -> Enemy)

datatype Player = Hero of (health * strength * move list ref * bag) 

datatype Choice = Fight | Forage | Eat

datatype Colors = RED | BLUE | GREEN | ORANGE | ARB of int

val player_max = 200

val enemy_names = [
  "Wild Balugaloo", 
  "Feral Pewpewpine", 
  "Spatula", 
  "Fearsome Skitterator",
  "Count Dorkula",
  "Splitter Splatter",
  "Elektrikal",
  "Puny Frogpole",
  "Skedankedanker",
  "Skaboose"
]

(* 
 * Helpers 
 *
 *   In which we realize we can never truly
 *   venture out on our own
 *)

fun max (a, b) = if a > b then a else b
fun min (a, b) = if a < b then a else b

val esc = (String.str (Char.chr 27))

(* Request Text from the user *)
fun prompt s =
let
  val _ = TextIO.output(TextIO.stdOut, s^" ")
  val _ = TextIO.flushOut(TextIO.stdOut)
  val result = TextIO.inputLine TextIO.stdIn
in
  case result
    of NONE => raise (GameOver "EOF received")
     | SOME x => String.substring(x, 0, (String.size x)-1)
end

(* Fun with ansi escape codes (tm) *)
fun get_color x = esc^"[38;5;"^(Int.toString x)^"m"

fun color s c =
 (case c
    of RED => get_color 160
     | BLUE => get_color 33
     | GREEN => get_color 42
     | ORANGE => get_color 202
     | ARB x => get_color x)^s^
 esc^"[0m"

fun smult s 0 = ""
  | smult s n = 
     if n < 0 then "" 
              else s^(smult s (n-1))

(* There's probably a built-in for div with ceil, but eh *)
fun cdiv (x, y) =
let
  val d = x div y
in
  if (d * y) <> x then d+1 else d
end

infix 5 cdiv 



(* MLton and SML/NJ use different Random libraries so we have this instead *)
val rng = ref (Int.fromLarge ((Time.toMilliseconds (Time.now ()))
                               mod (Int.toLarge (List.length enemy_names))))

fun getIdx () =
  (rng := ((!rng) * 1001017) mod (List.length enemy_names);
   !rng)

(* Global Definitions *)
val should_capture = ref false

val has_captured = ref false

val captured = ref Nothing

val posessing = ref false

val name = prompt ("Welcome, mighty hero, to the abyss of "
        ^(color "Everland" BLUE)^". Pray tell, "
        ^"what is your name?")

val _ = TextIO.print "\n"

(* No Peaking! *)

fun get_flag () =
  "pctf{Fake flag: please run on server}"

(* 
 * Attacks 
 *
 *   In which we hone our skills and
 *   prepare to do battle
 *)

fun kill_fn (my_h, my_s, their_h, their_s) =
let
  val h = !their_h
in
  (* It kills you. You're dead *)
  ((fn () => their_h := 0), (fn () => their_h := h))
end 

fun lunge_fn (my_h, my_s, their_h, their_s) =
let
  val th = !their_h
  val mh = !my_h
in
  (fn () => (their_h := 2*(!their_h) div 3; my_h := max(!my_h-10, 0)),
   fn () => (their_h := th; my_h := mh))
end

fun strike_fn (my_h, my_s, their_h, their_s) =
let
  val th = !their_h
in
  (fn () => (their_h := (max((!their_h)-15, 0))), fn () => (their_h := th))
end

fun empower_fn (my_h, my_s, their_h, their_s) =
let
  val mh = !my_h
  val ms = !my_s
in
  (fn () => (my_s := (!my_s + 20); my_h := max(!my_h - 20, 0)),
   fn () => (my_s := ms; my_h := mh))
end

fun recoup_fn (my_h, my_s, their_h, their_s) =
let
  val mh = !my_h
  val ms = !my_s
in
  (fn () => (my_s := max(!my_s - 20, 0); my_h := (!my_h + 10)),
   fn () => (my_s := ms; my_h := mh))
end

fun capture_fn (my_h, my_s, their_h, their_s) =
  ((fn () => should_capture := true), 
   (fn () => should_capture := false))

fun stink_fn (my_h, my_s, their_h, their_s) =
let
  val ts = !their_s
in
  (fn () => (their_s := max(!their_s - 10, 0)),
   fn () => (their_s := ts))
end

fun wrap_fn (my_h, my_s, their_h, their_s) =
let
  val th = !their_h
  val ts = !their_s
in
  (fn () => (their_s := max(!their_s - 5, 0); their_h := max(!their_h - 5, 0)),
   fn () => (their_s := ts; their_h := th))
end

fun pass_fn _ =
  (fn () => (), fn () => ())

val strike = ("Sword Strike", strike_fn)
val kill  = ("Death Wave", kill_fn)
val lunge = ("Spear Lunge", lunge_fn)
val empower = ("Full Empower", empower_fn)
val pass = ("Skip Turn", pass_fn)
val recoup = ("Recouperate", recoup_fn)
val capture = ("Capture", capture_fn)
val stink = ("Stink Out", stink_fn)
val wrap = ("Vine Wrap", wrap_fn)

(* Ok this is a hack. But at least I admit that *)
val nop = (0.0, ("Pass", fn () => ()))

(* 
 * Control Flow Logic 
 * 
 *   In which we weave a thrilling tale
 *   Of pain sorrow, and pwnage
 *)

fun get_opt () =
let
  val opt = prompt( 
        "Are you ready for your next fight? You can:\n"
       ^"  - "^(color "fight\n" GREEN)
       ^"  - "^(color "forage\n" GREEN)
       ^"  - "^(color "use\n" GREEN)
       ^"  >")
in
  if opt = "fight" then Fight else
  if opt = "forage" then Forage else
  if opt = "use" then Eat else
  (TextIO.print "Sorry, what was that?\n"; get_opt())
end

fun state_heuristic (arena as (my_h, my_s, their_h, their_s)) (n, move_fn) =
let
  val (activate, deactivate) = move_fn arena
  val _  = activate ()
  val mh = real(!my_h)
  val ms = real(!my_s)
  val th = real(!their_h)
  val ts = real(!their_s)
  val _  = deactivate ()
in
  ((ms/ts) + 3.0*(mh/th), (n, activate))
end 

(* Looks like a garbage collector spilled their load *)
fun print_stats (Hero(p_h, p_s, p_ms, bag)) (Opponent(e_h, e_s, e_ms, e_name, _)) =
  TextIO.print (
    "\n"^name^" ("^(color ((Int.toString (!p_s))^"st") GREEN)^") ["^
      (smult (color "|" GREEN) (((!p_h) * 10 div player_max ))) ^
      (smult " " (((player_max - (!p_h)) * 10 cdiv player_max))) ^ "] -- "^
    e_name^" ("^(color ((Int.toString (!e_s))^"st") RED)^"): "^
    (color ((Int.toString (!e_h))^"hp") RED)^"\n\n"
  )
  | print_stats _ _ = ()

fun get_choice opts col =
  let     
    val move_names = List.map (fn (n, _) => color n col) opts
    val (_, move_str) = List.foldl (fn (name, (n, msg)) =>
      (n+1, msg^"  - ("^(Int.toString n)^") "^name^"\n")) (0, "") move_names
    val _ = TextIO.print (move_str^"\n")
    val choice = Int.fromString (prompt ">") 
  in
    case choice
      of NONE => get_choice opts col
       | SOME x => get_elmt x opts opts col
  end
and get_elmt n [] opts col = get_choice opts col
  | get_elmt 0 (move::ms) _ _ = move
  | get_elmt n (_::ms) opts col = get_elmt (n-1) ms opts col


(* Fight! Fight! Fight! Fight! *)
fun fight (hero as Hero(p_h, p_s, p_ms, bag)) 
  (enemy as (Opponent (e_h, e_s, e_ms, e_name, next))) =
let
  val _ =
      if (!posessing) then
        (posessing := false;
         TextIO.print ("An "^(color "eerie" RED)^" wind rushes past, and"
                      ^" a fallen foe rises again...\n\n"))
      else
      let
        val arena = (e_h, e_s, p_h, p_s)
        val options = List.map (state_heuristic arena) e_ms
        val (_, (name, activate)) = List.foldl (fn (ad as (a, _), bd as (b, _)) =>
          if a > b then ad else bd) nop options
        val _ = TextIO.print (e_name^" used "^name^"!\n")
      in
        activate () 
      end
in
  if (!p_h) <= 0 then
    raise GameOver "You Died!"
  else
    let
      val _ = print_stats hero enemy
      val _ = TextIO.print "Available Moves:\n"
      val (name, init) = get_choice (!p_ms) RED
      val _ = TextIO.print ("Using: "^(color name RED)^"\n")
      val (act, _) = init (p_h, p_s, e_h, e_s)
      val _ = act()
      val _ = if (!p_h) <= 0 then
          raise GameOver "You Killed Yourself!"
        else ()
    in
    if (!should_capture) andalso (not (!has_captured)) 
    then
      if (!e_h > 50) then
        (TextIO.print ("It was too strong, you failed to capture "^
          (color e_name ORANGE));
        enemy)
      else
      let
        val _ = should_capture := false
        val _ = has_captured := true
        val _ = captured := enemy
        (* Kill them so that you can heal yourself *)
        fun sacrifice_fn (my_h, my_s, their_h, their_s) =
          (fn () => (
             my_h := min((!my_h)+min(!e_h, !my_s*10), player_max);
             e_h  := (!e_h-(!my_h)*10);
             
             p_ms := List.filter (fn (n, _) => n <> "Sacrifice") (!p_ms)),
           fn () => ()) (* Only used by the AI, not us *)
        val _ = p_ms := (List.filter (fn (n, _) => n <> "Capture") (!p_ms))
                        @[("Sacrifice", sacrifice_fn)]
      in
        next
      end
    else if (!e_h) <= 0 then (TextIO.print ("You Killed "^(color e_name
      ORANGE)^"!\n"); next) else enemy
    end
end
  | fight _ _ = raise Malformed


(* Forage! Forage! Forage... Forage? *)      
fun forage (Hero (_, _, _, bag)) wilderness =
  case (!wilderness)
    of [] => TextIO.print "You look around, but find nothing!\n"
     | ((item as (name, (_, _, _)))::rest) =>
     let
       val _ = TextIO.print ("Collected "^(color name BLUE)^"!\n")
       val _ = bag := (item :: (!bag))
     in
       wilderness := rest
     end

(* Use! Use! Ok, you get the point *)
fun use (hero as Hero(p_h, p_s, p_ms, bag)) =
  case (!bag)
    of [] => TextIO.print "No Available Items!\n"
     | bg =>
        let
          val _ = TextIO.print "Available Items:\n"
          val (name, (hp, st, mvs)) = get_choice bg BLUE
          val _ = TextIO.print ("Using: "^(color name BLUE)^"\n")
          val _ = p_h := max(!p_h, hp)
          val _ = p_s := max(!p_s, st)
          val _ = bag := List.filter (fn (n, _) => n <> name) (bg)
          val _ = p_ms := (!p_ms)@mvs
        in
          ()
        end

fun play_game hero Flag world _ =
  (TextIO.print ("Wow, looks like you beat all the enemies!\n"
                ^"Guess you deserve a flag: "); raise (CatFlag (get_flag())))
  | play_game hero (Init f) world original =
    play_game hero (f original) world original
  | play_game hero enemy world original =
  case (print_stats hero enemy; get_opt ())
    of Fight => play_game hero (fight hero enemy) world original
     | Forage => (forage hero world; play_game hero enemy world original)
     | Eat => (use hero; play_game hero enemy world original)
     (* Needs more: play_game hero enemy world original *)
  
fun find_best (this as (Opponent (_, my_s, _, _, next))) best entity =
  if (!my_s) > best then find_best next (!my_s) this
                    else find_best next best entity
  | find_best _ _ entity = entity


fun gen_enemies 0 = Init (fn e =>
  case (find_best e 0 Nothing)
    of (Opponent (health, strength, _, name, _)) =>
       (health    := max((!strength)*5, 250);
        strength  := max((!strength)*5, 250);
        posessing := true;
        Opponent (health, strength, [kill], "Posessed "^name, Flag))
     | _ => raise (GameOver "Boooo, the phantom never appeared...."))
  | gen_enemies n = Opponent(ref 80, ref 50, [
        lunge, 
        strike, 
        empower, 
        recoup
      ], List.nth (enemy_names, getIdx ()), gen_enemies (n-1))

fun start () =
let
  val wilderness = ref [
        ("Gross Weed", (20, 20, [stink])),
        ("Risky Dust", (0, 35, [])),
        ("Random Vines", (50, 0, [wrap])),
        ("Sacrificial Net", (0, 0, [capture])),
        ("Lucky Elixir", (100, 100, []))
  ]
  (* Hey, count yourself lucky. I could have made it 100 *)
  val num_enemies = 10

  val hero = Hero(ref 200, ref 100, ref [strike, empower, recoup, pass], 
        ref [("Max Health Potion", (200, 0, [])), ("Sharpened Dagger", (0, 100, []))])

  val _ = TextIO.print ("Well, "^(color name GREEN)^". It is valiant of you to venture here, but "
        ^(color "Everland" BLUE)^" is a place of darkness and despair.\nFew adventurers "
        ^"have dared descend these halls, and fewer have returned alive.\n"
        ^"Good luck, and godspeed.\n\n")

  val enemies = gen_enemies num_enemies
  val _ = (play_game hero enemies wilderness enemies)
    handle (GameOver msg) => (TextIO.print (color ("GameOver: "^msg) RED))

  val _ = TextIO.print "\nAnd thus, another passes to dust...\n"
in
  ()
end

(* 
 * Start
 * 
 *   In which our tale thusly begins
 *   Join us, dear friend
 *) 

val _ = start()
  handle (CatFlag f) => TextIO.print (color (f^"\n\n") (ARB 200))
