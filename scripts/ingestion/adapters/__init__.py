"""Source adapters for the ingestion framework."""

from .curated_json import AwesomeVLAAdapter, AwesomeHumanoidAdapter
from .progress_json import ProgressJsonAdapter
from .arxiv_rss import ArxivRssAdapter
from .unitree_api import UnitreeNewsAdapter
from .nvidia_rss import NvidiaRssAdapter
from .wechat_article import WechatArticleAdapter
from .robotics_tomorrow import RoboticsTomorrowAdapter
from .ieee_spectrum import IeeeSpectrumRoboticsAdapter
from .iso_standards import IsoRoboticsAdapter
from .actuator_suppliers import ActuatorSuppliersAdapter

__all__ = [
    "AwesomeVLAAdapter",
    "AwesomeHumanoidAdapter",
    "ProgressJsonAdapter",
    "ArxivRssAdapter",
    "UnitreeNewsAdapter",
    "NvidiaRssAdapter",
    "WechatArticleAdapter",
    "RoboticsTomorrowAdapter",
    "IeeeSpectrumRoboticsAdapter",
    "IsoRoboticsAdapter",
    "ActuatorSuppliersAdapter",
]
