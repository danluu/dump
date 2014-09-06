const test_dir = "jl_input"
const max_rand_string_len = 10

function generate_rand_strings(n::Int)
    for i in 1:n
        len = rand(1:2^19-5000)
        f = open("$(test_dir)/$(i)","w")
        write(f, randstring(len))
        close(f)
    end
end

# generate_rand_strings(3)

function checkable_name(name)
    typeof(eval(name)) == Function && isgeneric(eval(name))
#    || typeof(eval(name)) == DataType # killing for now because we can't call start on DataType 'methods'
end

function gen_rand_fn(name)    
    #        print("$name\n")
    methods_of_name = methods(eval(name))
    some_method = start(methods_of_name)
    #        print("$some_method type:$(typeof(some_method))\n")
    #        print("  sig: $(some_method.sig) type:$(typeof(some_method.sig))\n")
    some_sig = some_method.sig
    args = generate_rand_data(some_sig)
    if args != ""
        return("$name($args)\n")
    else 
        return ""
    end
end

function bogus()
    potential_names = sort(names(Base)) # names are returned in a random order.
    potential_names = filter(checkable_name, potential_names)
    fn_text = ""
    while fn_text == ""
        name = potential_names[rand(1:end)]
        print("$name\n")
        fn_text = gen_rand_fn(name)
    end
    print(fn_text)
end

function generate_rand_data(t::DataType)
    if t == String
        return string("\"",randstring(rand(1:max_rand_string_len)),"\"")
    elseif t == Int || t == Integer
        return string(rand(Int))
    end
    return ""
end

function generate_rand_data(sig::Tuple)
    can_generate = true
    args = ""
    for t in sig        
#        print("  t: $t $(typeof(t))\n")
        if typeof(t) == DataType
            randarg = generate_rand_data(t)
            if randarg != ""
                args = "$args$randarg,"
            end
        else
            # Likely a union type, which should be handled
            # by picking one of its types.
            can_generate = false
        end
#        print("    args: $args\n")
    end
        
    if can_generate
        # delete trailing comma.    
        return args[1:length(args)-1]
    else
        return ""
    end
end

bogus()


