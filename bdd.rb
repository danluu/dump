#!/usr/bin/ruby
#toy implementation of if-then-else for shared binary decision diagrams. Uses implicit memoization instead of explicitly consulting a unique table; this is probably both slower and more confusing :)

def memo(name,initialize = false)
  cache = {}; lastid = nil
  (class<<self; self; end).send(:define_method, name) do |*args|
    g = args.shift #don't care if graph has been updated                                                                         
    g.each_with_index{|node,ptr| cache[node] = ptr} unless (!initialize || g.object_id == lastid); lastid = g.object_id   #re-initialize cache if we switch to a different graph, but don't initialize ite!

    return cache[args] if cache.has_key? args
    cache[args] = super
  end
end

def smallest_var(g,*args)
  smallest_ptr = args.select{|p| g[p][0]}.sort_by{|p| g[p][0]}.first   #select is here to clear out nil entries. Could simplify this using andand
  g[smallest_ptr][0]
end

def cofactor(g,ptr,var,type) #type = 0 or 1 for low and high cofactor, respectively
  var == g[ptr][0] ? g[ptr][type+1] : ptr
end

def get_node_and_update_g(g,var,low,high) #yucky function with side effects: returns a pointer to the given node, and modifies g to add the node if it doesn't already exist. Must be memoized to work correctly (as written)
  if(low == high)
    low
  else
    g.push [var,low,high]
    g.length - 1
  end
end
memo(:get_node_and_update_g, true)

def ite(g,i,t,e) #takes a graph of a shared BDD, and pointers to three root notes
  return i if t == 1 && e == 0
  return t if i == 1 || e == t
  return e if i == 0

  sv = smallest_var(g,i,t,e)  
  x_low = ite(g,cofactor(g,i,sv,0),cofactor(g,t,sv,0),cofactor(g,e,sv,0))
  x_high = ite(g,cofactor(g,i,sv,1),cofactor(g,t,sv,1),cofactor(g,e,sv,1))

  return get_node_and_update_g(g,sv,x_low,x_high)
end
memo(:ite)

#array of [variable,low ptr,high ptr]
g0 = [[nil,false,false],[nil,true,true],[0,3,1],[1,0,1],[2,0,1],[0,0,4],[1,7,1],[3,0,1]]
g1 = [[nil,false,false],[nil,true,true],[0,3,1],[1,0,1],[2,0,1],[0,0,4],[1,7,1],[3,0,1]]

#tests for terminating cases
puts ite(g0,0,4,5) == 5
puts ite(g0,1,4,5) == 4
puts ite(g0,7,3,3) == 3

#test memoization of get_node_and_update_g
puts get_node_and_update_g(g1,0,3,1) == 2
puts g1 == [[nil,false,false],[nil,true,true],[0,3,1],[1,0,1],[2,0,1],[0,0,4],[1,7,1],[3,0,1]]
puts get_node_and_update_g(g1,0,3,1) == 2
puts g1 ==  [[nil,false,false],[nil,true,true],[0,3,1],[1,0,1],[2,0,1],[0,0,4],[1,7,1],[3,0,1]]

#simple test case for ite
puts ite(g0,2,5,6) == 9
puts g0 == [[nil, false, false], [nil, true, true], [0, 3, 1], [1, 0, 1], [2, 0, 1], [0, 0, 4], [1, 7, 1], [3, 0, 1], [1, 7, 0], [0, 8, 4]]
