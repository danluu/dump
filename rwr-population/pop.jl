# Grab data from http://modulaatio.com/rwr_server_list/player_count_graph.php

# using Gadfly
using Dates
using DataFrames

# First two digits of population is randomly wrong sometimes
# For example, 9 is 1009, 2009, or 3009
# This is easy to work around since population is never above 100, let alone 1000
function fix_pop_glitches(x::Int)
    fixed_pop = x % 1000    
    assert(fixed_pop < 900)
    return fixed_pop
end

function grab_pop(fname::String)
    f = open(fname)
    lines = readlines(f)
    pop_match = r"(\d+)\]"
    time_match = r"setTime\((\d+)\)"
    time_lines = filter(time_match, lines)
    data_lines = filter(pop_match, lines)
    data::Array{Int} = map(l -> int(match(pop_match, l).captures[1]), data_lines)
    data = map(fix_pop_glitches, data)
    # Not using DateTime because there's a bug in Gadfly that seems to be pretty old
    # that makes DateTime dataframes blow up. Not sure if/when it will be fixed.
    # times::Array{DateTime} = 
    # map(l -> 
    #     unix2datetime(int(match(time_match, l).captures[1]) / 1000),
    #     time_lines)
    times::Array{Int} = 
    map(l -> 
        iround(int(match(time_match, l).captures[1]) / (1000 * 60)),
        time_lines)
    
    df = DataFrame(x=times, y=data, label="Players")    
end

# function plot_junk(data::Array{Int})
#     mdata = map(x->min(1,x) , data)

#     sdata = [mean(data[i-118:i]) for i = 119:length(data)]
#     smdata = [mean(mdata[i-118:i]) for i = 119:length(mdata)]
#     plot(x=1:length(sdata), y=sdata, Geom.line, 
#          layer(Geom.smooth, Theme(default_color=color("red"))))

#     plot(x=1:length(smdata), y=smdata, Geom.line, 
#          layer(Geom.smooth, Theme(default_color=color("red"))))

#     plot(x=1:length(sdata), y=sdata, Geom.line, layer(Geom.smooth, Theme(default_color=color("red"))))

# end

# grab_pop("raw.data")


function heinous_bug_workaround(df::DataFrame)
    start_time = df[1][1]
    end_time = df[1][end]
    
    len = end_time - start_time + 1
    arr = Array(Int8, len)
    for i in 1:size(df,1)-1
        idx = df[1][i] - start_time + 1
        idx_n = df[1][i+1] - start_time + 1
        # println("Setting $idx:$idx_n to $(df[2][i])")
        for j in idx:idx_n
            arr[j] = df[2][i]
        end
    end
    arr
end

function daily_average()
    df = grab_pop("raw.data")
    a = heinous_bug_workaround(df)
    sa::Array{Float32} = [mean(a[i-1339:i]) for i = 1440:length(a)]
end

function daily_zero_pop()
    df = grab_pop("raw.data")
    a::Array{Int8} = heinous_bug_workaround(df)
    a = map(x -> min(x, 1), a)
    sa::Array{Float32} = [mean(a[i-1339:i]) for i = 1440:length(a)]
end

function squash(x, n)
    if x <= n
        0
    else
        1
    end
end

function daily_n_pop(n::Int)
    df = grab_pop("raw.data")
    a::Array{Int8} = heinous_bug_workaround(df)
    a = map(x -> squash(x, n), a)
    sa::Array{Float32} = [mean(a[i-1339:i]) for i = 1440:length(a)]
end

function plot_daily_n_pops()
    sa1 = daily_n_pop(1)
    sa5 = daily_n_pop(5)
    sa10 = daily_n_pop(10)
    sa20 = daily_n_pop(20)

    plot(layer(x=1:length(sa1), y=sa1, Geom.line), layer(x=1:length(sa1), y=sa1, Geom.smooth, Theme(default_color=color("red"))),
         layer(x=1:length(sa5), y=sa5, Geom.line), layer(x=1:length(sa5), y=sa5, Geom.smooth, Theme(default_color=color("red"))),
         layer(x=1:length(sa10), y=sa10, Geom.line), layer(x=1:length(sa10), y=sa10, Geom.smooth, Theme(default_color=color("red"))),
         layer(x=1:length(sa20), y=sa20, Geom.line), layer(x=1:length(sa20), y=sa20, Geom.smooth, Theme(default_color=color("red")))
         )
end
