module View exposing (..)

import Html exposing (Html, div, text)
import Msgs exposing (Msg)
import Models exposing (Model)

-- VIEW
view : Model -> Html.Html Msg
view model = Html.div []
             [Html.text model]
