// Mega Hello World
// Take two command-line parameters and then print them along with the current time to the console. 

open System

[<EntryPoint>]
let main (args: string[]) =

// whitespace is important, it denotes code blocks, as seen in this if block; if failwith was four spaces back, this could would not run. 
    if args.Length <> 2 then
        failwith "Error: Expected arguments <greeting> and <thing>"
    

    // let binds a name to an immutable (unchanging) case-sensitive values
    // A value name can be [A-Za-z_0-9`]

    let greeting, thing = args.[0], args.[1]
    let TimeOfDay = DateTime.Now.ToString("hh:mm tt")

    printfn "%s, %s at %s" greeting thing TimeOfDay

    // Program exit code
    0

// Run the code in VSC using >FSI:Start and sending the following argument, since we can't edit the output window like VS
main [|"Hello"; "World" |]