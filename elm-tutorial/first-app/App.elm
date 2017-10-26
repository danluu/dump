module App exposing (..)

import Html
import Html.Events

-- MODEL
type alias Model =
    Bool

init : ( Model, Cmd Msg )
init =
    ( False, Cmd.none )


-- MESSAGES
type Msg
    = Expand | Collapse

-- VIEW
view : Model -> Html.Html Msg
view model =
    if model then
        Html.div []
            [Html.button [Html.Events.onClick Collapse] [Html.text "Collapse"]
            , Html.text "Widget"
            ]
    else
        Html.div []
            [Html.button [Html.Events.onClick Expand] [Html.text "Expand"]]

-- UPDATE
update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        Expand ->
            (True, Cmd.none)
        Collapse ->
            (False, Cmd.none)

-- SUBSCRIPTIONS
subscriptions : Model -> Sub Msg
subscriptions model =
    Sub.none

-- MAIN
main : Program Never Model Msg
main =
    Html.program
    { init = init
    , view = view
    , update = update
    , subscriptions = subscriptions
    }
