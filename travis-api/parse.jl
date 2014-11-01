using Dates

# Example usage: julia parse.jl cleaned/devops
# Produces name,pass_rate,fail_rate,error_rate

function process_travis_log(fname::String)
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
    println("$fname,$pass_rate,$fail_rate,$error_rate")
end

# Run on one directory. Not recurisve.
function process_logs(dir::String)
    for f in readdir(dir)
        if !ismatch(r"Gemfile.*",f)
            process_travis_log(string(dir,"/",f))    
        end
    end
end

process_logs(ARGS[1])
