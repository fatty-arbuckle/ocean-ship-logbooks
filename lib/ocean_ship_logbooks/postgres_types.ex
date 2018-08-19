defmodule PostgresTypes do
  Postgrex.Types.define(OceanShipLogbooks.PostgresTypes, [Geo.PostGIS.Extension] ++ Ecto.Adapters.Postgres.extensions(), json: Poison)
end
