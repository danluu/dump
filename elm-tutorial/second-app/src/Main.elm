module Main exposing (..)

import Html
import Msgs exposing (Msg)
-- import Models exposing (Model)
import Update exposing (update)
import View exposing (view)

-- MODEL
type alias Model = String

init : (Model, Cmd Msg)
init = ("Hello", Cmd.none)

-- SUBSCRIPTIONS
subscriptions : Model -> Sub Msg
subscriptions model = Sub.none                         

-- MAIN
main : Program Never Model Msg
main =
    Html.program
        { init = init
        , view = view
        , update = update
        , subscriptions = subscriptions
        }                      
