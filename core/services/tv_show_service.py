from core.clients.sample_api.futurama_client import FuturamaClient
from core.dtos.tv_show_dtos import Person, TvShow, TvShows


def get_shows():
    shows = []
    futurama = FuturamaClient().get_show_info()
    if futurama:
        years_aired = futurama.years_aired.split("–")
        show = TvShow(
            id=futurama.id,
            synopsis=futurama.synopsis,
            year_start=years_aired[0],
            year_stop=years_aired[1],
            creators=([Person(**creator.dict()) for creator in futurama.creators] if futurama.creators else None),
        )
        shows.append(show)

    return TvShows(shows=shows)
