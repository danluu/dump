module Msgs exposing (..)

import Http
import Models exposing (Player)
import Navigation exposing (Location)
import RemoteData exposing (WebData)

type Msg
    = ChangeLevel Player Int
    | OnFetchPlayers (WebData (List Player))
    | OnLocationChange Location
    | OnPlayerSave (Result Http.Error Player)
