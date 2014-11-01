using Dates

# Example usage: julia parse.jl cleaned/devops devops
# Produces category,name,pass_rate,fail_rate,error_rate

# This number of 9s nonsense is never used. Just playing with something.
# Convert a percent to colloqial "9s" measurement, as in 3 9s of reliability.
function number_of_9s(pct::Float64)
    if pct >= 1.0
        return float64(Inf)
    end
    
    base,remainder = base_number_of_9s(pct)
    if isnan(base) || isnan(remainder)
        return NaN
    end

    if base >= 0
        # println("log of $(remainder *10^(base+1)) is $(log(9,remainder * 10^(base+1)))")
        fraction = log(9, remainder * 10^(base+1))
        fraction = fraction < 0 ? 0 : fraction # Horrible hack for our weirdo not-quite log scale.
    else
        assert(false) # Shouldn't happen with our data.
    end
    return base + fraction
end

# Floor of number of 9s, i.e., number of 9s without fractional part.
# This is the worst hack ever written. I apologize to anyone reading this.
function base_number_of_9s(pct::Float64)
    if isnan(pct)
        return (NaN, pct)
    end

    assert(pct > .09)
    if pct < .9
        return (0, pct)
    elseif pct < .99
        return (1, pct-.9)
    elseif pct < .999
        return (2, pct-.99)
    elseif pct < .9999
        return (3, pct-.999)
    elseif pct < .99999
        return (4, pct-.9999)
    elseif pct < .999999
        return (5, pct-.99999)
    elseif pct < .9999999
        assert(false) # We don't ever hit this with our data.
    end
end

function process_travis_log(fname::String, category::String, project::String)
    lines = readlines(open(fname))
    time_in_status = Dict()

    last_time = nothing
    time_in_status["passed:"] = 0
    time_in_status["failed:"] = 0
    time_in_status["errored:"] = 0
    time_in_status["canceled:"] = 0
    time_in_status["started:"] = 0
    for line in lines
        # print(line)
        parts = split(line)        
        time_str = string(parts[1], ' ', parts[2])
        if time_str == "not yet"
            continue
        else
            time = DateTime(time_str, "y-m-d H:M:S")
        end
        status = parts[4]

        if last_time != nothing
            diff = div(int(last_time - time),1000) # difference in seconds
            if diff < 0
                # println("ERROR $fname $last_time $time")
            else
                time_in_status[status] += diff
            end
        end
        last_time = time
    end
    total_time = time_in_status["passed:"] + time_in_status["failed:"] + time_in_status["errored:"]
    pass_rate = time_in_status["passed:"] / total_time
    fail_rate = time_in_status["failed:"] / total_time
    error_rate = time_in_status["errored:"] / total_time
    nines = number_of_9s(pass_rate)
    println("$category,$project,$pass_rate,$fail_rate,$error_rate,$nines")
end

# Run on one directory. Not recurisve.
function process_logs(dir::String, category::String)
    for f in readdir(dir)
        if !ismatch(r"Gemfile.*",f)
            process_travis_log(string(dir,"/",f), category, f)
        end
    end
end

process_logs(ARGS[1], ARGS[2])
