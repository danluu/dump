a = 0.0 / 0.0
2.0.0-p247 :011 > [1.0, 2.0].min                                                                                                                                                     
 => 1.0 
2.0.0-p247 :012 > a
 => NaN 
2.0.0-p247 :013 > [1.0, a].min                                                                                                                                                       
ArgumentError: comparison of Float with 1.0 failed
