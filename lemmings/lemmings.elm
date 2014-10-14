import Keyboard
import Window

-- MODEL
type Lemming = {x:Int, y:Int, vx:Float, vy:Float, dir:String, onSurface:Bool}
mario1:Lemming
mario1 = { x=20, y=900, vx=0, vy=0, dir="right", onSurface=False }
mario2:Lemming
mario2 = { x=60, y=900, vx=0, vy=0, dir="right", onSurface=False }
allMarios = [mario1, mario2]

type Platform = {xmin:Int, xmax:Int, ymin:Int, ymax:Int}
platform0:Platform
-- Ground extends past edge to make sure we don't fall off if there's lag
platform0 = { xmin=-1000, xmax=2000, ymin = 0, ymax = 50 }
platform1:Platform
platform1 = { xmin=100, xmax=2000, ymin = 200, ymax = 250 }
platform2:Platform
platform2 = { xmin=0, xmax=400, ymin = 300, ymax = 315 }
allPlatforms = [platform0, platform1, platform2]

near: Lemming -> Platform -> Bool
near m platform = m.x < platform.xmax && m.x > platform.xmin

--centerPlatform: Platform -> (Float,Float)
--centerPlatform {xmin, xmax, ymin, ymax} = (toFloat(xmin + (xmax - xmin)/2), toFloat(ymin + (ymax - ymin)/2))

centerPlatform: Platform -> (Int, Int)
centerPlatform {xmin, xmax, ymin, ymax} = 
    ((xmin + (xmax - xmin)//2), (ymin + (ymax - ymin)//2))

throughPlatform: Float -> Lemming -> Platform -> Bool
throughPlatform t m p = (m.y <= p.ymax && m.y - (round (t*m.vy)) >= p.ymax) &&
  near m p
onPlatform m p = m.y == p.ymax && near m p
onSurface m p = onPlatform m p || m.y == 0

hitPlatform: Float -> Lemming -> [Platform] -> Maybe Platform
hitPlatform t m ps =
  case ps of
    [] -> Nothing
    p::shortnamesarebad -> 
      if throughPlatform t m p
        then Just p
      else 
        hitPlatform t m shortnamesarebad

-- UPDATE -- ("m" is for Mario)
gravity: Float -> Lemming -> Lemming
gravity t m = 
  case hitPlatform t m allPlatforms of
    Just p -> {m | vy <- 0, y <- p.ymax, onSurface <- True}
    Nothing -> { m | vy <- m.vy - t/4, onSurface <- False }
  
 
    
physics: Float -> Lemming -> Lemming
physics t m = { m | x <- m.x + (round (t*m.vx)) , y <- max 0 (m.y + (round (t*m.vy))) }

walk: Lemming -> Lemming
walk m = 
  if m.vx == 0 && m.onSurface
    then { m | vx <- 2, dir <- "right"}
  else if m.x > 990 && m.onSurface
    then { m | vx <- -2, dir <- "left"}
  else if m.x < 10 && m.onSurface
    then { m | vx <- 2, dir <- "right"}
  else
    m

step (dt, keys) = gravity dt >> walk >> physics dt


-- DISPLAY
renderPlatform (w,h) p =
  let (cx, cy) = centerPlatform p in
  rect ((toFloat(p.xmax - p.xmin))/1000 * w) ((toFloat(p.ymax - p.ymin))/1000 * h)
  |> filled (rgb 74 163 41)
  |> move ((toFloat cx)/1000 * w - w/2, ((toFloat cy)/1000 * h) - h/2)
  
renderMario (w',h') mario =  
  let 
    verb = if | not mario.onSurface -> "jump"
                | mario.vx /= 0 -> "walk"
                | otherwise     -> "stand"
    src = "/imgs/mario/" ++ verb ++ "/" ++ mario.dir ++ ".gif"
  in
  toForm (image 35 35 src) 
  |> move ((toFloat mario.x)/1000 * w' - w'/2, ((toFloat mario.y)/1000 * h') + 14 - h'/2)  
  

render (w',h') mario =
  let (w,h) = (toFloat w', toFloat h')
  in collage w' h'
      ([ rect w h  |> filled (rgb 174 238 238)
      , renderMario (w, h) mario
      ] ++ (map (renderPlatform (w,h)) allPlatforms))

-- MARIO
input = let delta = lift (\t -> t/20) (fps 60)
        in  sampleOn delta (lift2 (,) delta Keyboard.arrows)

main = lift2 render Window.dimensions foldp step allMarios input
