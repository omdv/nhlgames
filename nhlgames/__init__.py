from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution('NHLGames').version
except DistributionNotFound:
    __version__ = '(local)'
