module Models exposing (..)

-- MODEL
type alias Model = {players : List Player}

initialModel : Model
initialModel = {players = [Player "1" "Sam" 1]}

type alias PlayerId = String

type alias Player =
    { id : PlayerId
    , name : String
    , level : Int
    }
