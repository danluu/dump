module App exposing (..)

import Html
import Html.Events

-- MODEL
type alias Model = Int

init : ( Model, Cmd Msg )
init =
    ( 0, Cmd.none )


-- MESSAGES
type Msg = Increment Int

-- VIEW
view : Model -> Html.Html Msg
view model =
    Html.div []
        [Html.button [Html.Events.onClick (Increment 2)] [Html.text "+"]
        , Html.text (toString model)
        ]

-- UPDATE
update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        Increment howMuch ->
            (model + howMuch, Cmd.none)

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
