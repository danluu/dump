import Keyboard
import Window
import List
import Mouse

-- MODEL
type Lemming = {x:Int, y:Int, vx:Float, vy:Float, dir:String, onSurface:Bool}
mario1:Lemming
mario1 = { x=800, y=1050, vx=0, vy=0, dir="left", onSurface=False }
mario2:Lemming
mario2 = { x=840, y=1050, vx=0, vy=0, dir="left", onSurface=False }
mario3:Lemming
mario3 = { x=880, y=1050, vx=0, vy=0, dir="left", onSurface=False }
mario4 = { x=920, y=1050, vx=0, vy=0, dir="left", onSurface=False }
allMarios: [Lemming]
allMarios = [mario1, mario2, mario3, mario4]

type Platform = {xmin:Int, xmax:Int, ymin:Int, ymax:Int}
platform0:Platform
-- Ground extends past edge to make sure we don't fall off if there's lag
platform0 = { xmin=-1000, xmax=2000, ymin=0, ymax=50 }
platform1:Platform
platform1 = { xmin=100, xmax=2000, ymin=200, ymax=250 }
platform2:Platform
platform2 = { xmin=0, xmax=400, ymin = 300, ymax = 315 }
platform10 = { xmin=500, xmax=2000, ymin=1010, ymax=1040}
allPlatforms: [Platform]
allPlatforms = [platform0, platform1, platform2, platform10]

near: Lemming -> Platform -> Bool
near m platform = m.x < platform.xmax && m.x > platform.xmin

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
allGravity: Float -> [Lemming] -> [Lemming]
allGravity t ms = List.map (gravity t) ms

-- Fall unless on a surface
gravity: Float -> Lemming -> Lemming
gravity t m = 
  case hitPlatform t m allPlatforms of
    Just p -> {m | vy <- 0, y <- p.ymax, onSurface <- True}
    Nothing -> { m | vy <- m.vy - t/4, onSurface <- False }
  
 
allPhysics: Float -> [Lemming] -> [Lemming]
allPhysics t ms = List.map (physics t) ms

-- Add velocity to position
physics: Float -> Lemming -> Lemming
physics t m = { m | x <- m.x + (round (t*m.vx)) , y <- max 0 (m.y + (round (t*m.vy))) }


allWalk: a -> [Lemming] -> [Lemming]
allWalk mouse ms = List.map (walk mouse) ms

-- Set velocity when on surface
walk: a -> Lemming -> Lemming
walk mouse m = 
  if m.vx == 0 && m.onSurface
    then { m | vx <- 2, dir <- "right"}
  else if m.x > 990 && m.onSurface
    then { m | vx <- -2, dir <- "left"}
  else if m.x < 10 && m.onSurface
    then { m | vx <- 2, dir <- "right"}
  else
    m

-- convert from mouse coordinate system to our reference coordinate system
mouseToReference (x,y) (w,h) = (x, y-h)

step: (Float, a) -> [Lemming] -> [Lemming]
step (dt, mouse) = allGravity dt >> allWalk mouse >> allPhysics dt


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
  

render (w',h') marios =
  let (w,h) = (toFloat w', toFloat h')
  in collage w' h'
      ([ rect w h  |> filled (rgb 174 238 238)
      ] ++ (List.map (renderPlatform (w,h)) allPlatforms)
      ++ (List.map (renderMario (w,h)) marios))

-- MARIO
input = let delta = lift (\t -> t/20) (fps 60)
        in  sampleOn delta (lift2 (,) delta Mouse.position)

main = lift2 render Window.dimensions (foldp step allMarios input)
