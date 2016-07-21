# convert a single symbol, like foo_a_b_c into a function call, foo(a,b,c)
macro ʕ╯•ᴥ•ʔ╯︵‾‾(e)
    name = string(e)
    syms = parse_name(name)
    args = [parse(x) for x in syms[2:end]]
    f = symbol(syms[1])
    quote
        $(f)($(args...))
    end
end

macro call_fn(name, rest)
    syms = parse_name(string(rest))
    args = [parse(x) for x in syms]
    f = symbol(name)
    quote
        $(esc(f))($(args...))
    end
end
              
macro define_fn(name, args, body)
    quote
        function $(esc(symbol(name))) ($args)
            $body
        end
    end
end              
              
# convert a string to a function name and its arguments. Underscores are escaped by using an underscore
function parse_name(s)
    in_under = false
    symbols = String[""]
    for c in s
        if in_under
            if c == '_'
                symbols[end] *= "_"
            else
                push!(symbols,string(c))
            end
            in_under = false
        else
            if c == '_'
                in_under = true
            else
                symbols[end] *= string(c)
                in_under = false
            end
        end
    end
    symbols
end
