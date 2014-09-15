# Something is causing ARM results to be different from x86 results.
# It's probably not this simple, but you've got to start somewhere.
function do_rand_stuff()
    srand(1)
    for i in 1:10000
        println(rand(Int64))
    end
end

do_rand_stuff()
