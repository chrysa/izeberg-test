from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from typing import NoReturn

import requests
from requests import request


@dataclass
class PokeAccess:
    json_response_type: list[dict[str, int | str | list[dict[str, str]]]] = None
    poke_api: str = "https://pokeapi.co/api/v2"
    poke_api_type: str = None

    def __post_init__(self):
        self.poke_api_type: str = f"{self.poke_api}/type"
        self.poke_api_pokemon: str = f"{self.poke_api}/pokemon"
        self._get_pokemon_types()

    def _get_pokemon_types(self):
        self.json_response_type = self._request_as_json(url=self.poke_api_type)

    def _request_as_json(self, *, url: str) -> list[dict[str, Any]]:
        response: request = requests.get(url)
        return response.json()

    def get_type_list_name(self) -> list[str] | NoReturn:
        if self.json_response_type is None:
            raise Exception("POKE API don't return any types")
        else:
            return [value["name"].lower() for value in self.json_response_type["results"]]

    def get_type_id(self, *, poke_type: str) -> int:
        for value in self.json_response_type["results"]:
            if poke_type == value["name"]:
                return int(value["url"].split("/")[-2])

    def get_pokemon(self, *, pokemon: int) -> dict[str, Any]:
        return self._request_as_json(url=f"{self.poke_api_pokemon}/{pokemon}")

    def get_pokemon_list_by_type(self, *, type_name: str) -> list[str]:
        poke_type_id: int = self.get_type_id(poke_type=type_name)
        response: request = requests.get(f"{self.poke_api_type}/{poke_type_id}/")
        response_json: list[dict[str, int | str]] = response.json()
        return [poke["pokemon"]["name"] for poke in response_json["pokemon"]]
