module Update exposing (..)

import Msgs exposing (Msg(..))
import Models exposing (Model)

-- UPDATE
update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
    case msg of
        NoOp -> (model, Cmd.none)
