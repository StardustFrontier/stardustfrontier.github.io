# RDNH SV4 Language Features

[Return to Index](./docs.html)

#

This page summarizes any _new_ language features in SV4.\
Anything self-explanatory that was carried over from the original script version (SV3) might not be explained here.

## Values and Types
RDNH SV4 is a dynamically typed language and variables are allowed to change types at any time. This is different from DNH ph3, which did not allow types to change after the first assignment.

SV4's types are: _nil_, _bool_, _real_, _char_, _pointer_, _function_, _array_, _string_, and _table_\
_function_ may be shortened to _func_, this will behave the same in all contexts. Note that _pointer_ is currently unused, but reserved.

### New Types

#### Function Type

To obtain a _function_ value, write _$_ (dollar symbol) before the name of a function:
<pre>
function TestFunc() { WriteLog("meow"); }
let myFunc = $TestFunc;
WriteLog(myFunc); // "<function TestFunc>"
myFunc(); // "meow"
</pre>
Functions stored in variables behave much like normal functions, but have a small runtime cost to check their validity.

_**Important:**_ _function_ values cannot be shared across script boundaries. This means it's generally unsafe to store them in common data or pass them as event arguments.

#### Table Type

Tables are like custom objects and behave similarly to objects in Javascript.
<pre>
let myTable = {
  x = 123,
  y = 456,
  name = "mana"
};
let fieldY = "y";

// access 'x' field of myTable
WriteLog(myTable.x);

// alternate form of accessing 'y' field, allows for field access
// using variables
WriteLog(myTable[fieldY]);

WriteLog(myTable.name); // mana
</pre>

### Literals
<pre>
WriteLog(nil);              // nil literal (absence of value)
WriteLog(true, false);      // boolean literals
WriteLog(69, 420.0);        // real literal (base 10)
WriteLog(0xCA7F00D);        // real literal (hexadecimal)
WriteLog('a');              // char literal
WriteLog("cat");            // string literal
WriteLog( [0, 1, 2] );      // array literal
WriteLog( {x = 1, y = 2} ); // table literal (like objects in JS)
</pre>

### Variable Declaration
Variables can be declared using _let_, _var_, or _const_. When declared with _let_ or _var_ the variable will be reassignable, while with _const_ the variable will not be reassignable. When a variable is marked as const, the compiler will also attempt to perform a very basic form of constant propagation, where the constant's value will be compiled directly into the bytecode instead of loading/storing the variable. Currently, this optimization only works when a literal value is assigned.

_Note_: Variables that have not yet been assigned to are implicitly initialized with `nil`.

Example:
<pre>
let x = 123;
WriteLog(x); // 123.0
x = "hello";
WriteLog(x); // hello

const y = 456;
WriteLog(y); // 456.0
y = "world"; // error: can't assign to constant variable

let z;
WriteLog(z); // nil
WriteLog(x + z); // error: can't add 'real' and 'nil'
</pre>

### Type Annotations
Optionally, variables and function parameters may be annotated with 'hints' to suggest what type is stored in them to the _scripter_. These are not enforced by the compiler and are only meant to serve as a way to document your code without excessive comments.

Example:
<pre>
let cat: string = "mana";
cat = 69; // It's not a string anymore!!

// this is a function named CountSheep that takes an
// array of strings named 'sheep' and returns a 'real' value
function CountSheep(sheep: array[string]): real {
    return length(sheep);
}
</pre>

## Blocks

### Async Block
A new type of block called _async_ has been ported from ph3sx.\
These are simply nameless tasks that execute immediately.

Example:
<pre>
async {
    WriteLog("hello");
    wait(60);
    WriteLog("world");
}
</pre>
The above would be equivalent to the following in execution:
<pre>
task MyTask() {
    WriteLog("hello");
    wait(60);
    WriteLog("world");
}

MyTask();
</pre>

### Difficulty Switch
A new type of block/statement called the _difficulty switch_ has beeen added.\
These are like if statements that execute if _GetDifficulty_ is equal to any of the specified difficulties, which are letters representing the index of the difficulty.

The letters used for difficulty switches can be defined in rdnh.def with the _ScriptDifficultyLetters_ property, which by default is _ENHLXPOZ_.

Example:
<pre>
!EN {
    WriteLog("Executes on easy or normal difficulties");
}

!H: WriteLog("Executes on hard difficulty (single-statement version)");

!L {
    WriteLog("Executes on lunatic dificulty")
}
</pre>

### Scoping Behaviour
Curly braces can be used to define _blocks_. A block is a series of statements with a scope.

**Note:** The keyword _local_ is a deprecated way to create a new block and should be omitted in new code.
<pre>
if (mana == "cat") { // new block starts after {
    let sound = "meow";
    WriteLog(sound); // statement
} // block ends here, local variable 'sound' is discarded as it is unreachable
</pre>

The following is an example of how variables are scoped in blocks:
<pre>
{
    let a = 1;
    {
        let b = 2;
        WriteLog(a, b); // 1 2
        {
            let c = 3;        
            WriteLog(a, b, c); // 1 2 3
        } // c is no longer accessible after this brace
    } // b is no longer accessible after this brace
    WriteLog(a); // 1
}
</pre>

Variables may be _shadowed_ within a lower scope and even initialized with a variable of the same name from an upper scope.
<pre>
{
    let a = 1;
    {
        // performance is improved in some cases by making a local 
        // reference to a variable from an upper scope
        let a = a;
        a += 68;
        WriteLog(a); // 69
    }
    WriteLog(a); // 1
}
</pre>

## Operators
- Bitwise operators have been added with the same precedence as Python
- The power operator from DNH ph3 has been changed from ^ to **
  - The ^ operator now refers to bitwise XOR

## Loops

### Normal Loop
The usage of the _loop_ keyword is unchanged in SV4.
<pre>
loop (3)
    WriteLog("meow");
</pre>
Result: The string "meow" is printed 3 times.

### Ascent and Descent

#### Basic Form
As in SV3, the standard Danmakufu _ascent_ and _descent_ loops are available:
<pre>
ascent (i in 0..3)
    WriteLog(i);
</pre>
Result: The values 0.0, 1.0, then 2.0 are printed, while using `descent` would print the same values in reverse.

#### 'Each' Form
SV4 adds in a new 'each' version of these loops which iterates over collection types like arrays, strings, and tables:
<pre>
ascent (c in "meow")
    WriteLog(c);
</pre>
Result: The character values 'm', 'e', 'o', 'w' are printed. If `descent` was used, then it would print 'w', 'o', 'e', 'm'. This allows for easy reversal of arrays and strings.