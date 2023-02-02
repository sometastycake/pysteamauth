from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import List
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper


ALLOW_FIELD_NAMED_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
DESCRIPTOR: _descriptor.FileDescriptor
FORCE_PHP_GENERATION_FIELD_NUMBER: _ClassVar[int]
MSGPOOL_HARD_LIMIT_FIELD_NUMBER: _ClassVar[int]
MSGPOOL_SOFT_LIMIT_FIELD_NUMBER: _ClassVar[int]
PHP_OUTPUT_ALWAYS_NUMBER_FIELD_NUMBER: _ClassVar[int]
allow_field_named_steam_id: _descriptor.FieldDescriptor
force_php_generation: _descriptor.FieldDescriptor
k_EBanContentCheckResult_Likely: EBanContentCheckResult
k_EBanContentCheckResult_NeedsChecking: EBanContentCheckResult
k_EBanContentCheckResult_NotScanned: EBanContentCheckResult
k_EBanContentCheckResult_Possible: EBanContentCheckResult
k_EBanContentCheckResult_Reset: EBanContentCheckResult
k_EBanContentCheckResult_Unlikely: EBanContentCheckResult
k_EBanContentCheckResult_VeryLikely: EBanContentCheckResult
k_EBanContentCheckResult_VeryUnlikely: EBanContentCheckResult
k_EClanBetaReleaseEvent: EProtoClanEventType
k_EClanBroadcastEvent: EProtoClanEventType
k_EClanChatEvent: EProtoClanEventType
k_EClanCrosspostEvent: EProtoClanEventType
k_EClanDLCReleaseEvent: EProtoClanEventType
k_EClanDevStreamEvent: EProtoClanEventType
k_EClanESportTournamentStreamEvent: EProtoClanEventType
k_EClanFamousStreamEvent: EProtoClanEventType
k_EClanFreeTrial: EProtoClanEventType
k_EClanFutureReleaseEvent: EProtoClanEventType
k_EClanGameEvent: EProtoClanEventType
k_EClanGameItemSalesEvent: EProtoClanEventType
k_EClanGameReleaseEvent: EProtoClanEventType
k_EClanGameSalesEvent: EProtoClanEventType
k_EClanIRLEvent: EProtoClanEventType
k_EClanInGameBonusXPEvent: EProtoClanEventType
k_EClanInGameChallengeEvent: EProtoClanEventType
k_EClanInGameContentReleaseEvent: EProtoClanEventType
k_EClanInGameContestEvent: EProtoClanEventType
k_EClanInGameEventGeneral: EProtoClanEventType
k_EClanInGameLootEvent: EProtoClanEventType
k_EClanInGamePerksEvent: EProtoClanEventType
k_EClanMajorUpdateEvent: EProtoClanEventType
k_EClanMeetingEvent: EProtoClanEventType
k_EClanMusicAndArtsEvent: EProtoClanEventType
k_EClanNewsEvent: EProtoClanEventType
k_EClanOtherEvent: EProtoClanEventType
k_EClanPartyEvent: EProtoClanEventType
k_EClanPreAnnounceMajorUpdateEvent: EProtoClanEventType
k_EClanSeasonRelease: EProtoClanEventType
k_EClanSeasonUpdate: EProtoClanEventType
k_EClanSmallUpdateEvent: EProtoClanEventType
k_EClanSpecialCauseEvent: EProtoClanEventType
k_EClanSportsEvent: EProtoClanEventType
k_EClanTripEvent: EProtoClanEventType
k_EEventBroadcastStart: PartnerEventNotificationType
k_EEventMatchStart: PartnerEventNotificationType
k_EEventPartnerMaxType: PartnerEventNotificationType
k_EEventStart: PartnerEventNotificationType
msgpool_hard_limit: _descriptor.FieldDescriptor
msgpool_soft_limit: _descriptor.FieldDescriptor
php_output_always_number: _descriptor.FieldDescriptor


class CBilling_Address(_message.Message):
    __slots__: List[str] = ["address1", "address2", "city", "country_code", "first_name", "last_name", "phone",
                            "postcode", "us_state", "zip_plus4"]
    ADDRESS1_FIELD_NUMBER: _ClassVar[int]
    ADDRESS2_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    POSTCODE_FIELD_NUMBER: _ClassVar[int]
    US_STATE_FIELD_NUMBER: _ClassVar[int]
    ZIP_PLUS4_FIELD_NUMBER: _ClassVar[int]
    address1: str
    address2: str
    city: str
    country_code: str
    first_name: str
    last_name: str
    phone: str
    postcode: str
    us_state: str
    zip_plus4: int

    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ...,
                 address1: _Optional[str] = ..., address2: _Optional[str] = ..., city: _Optional[str] = ...,
                 us_state: _Optional[str] = ..., country_code: _Optional[str] = ..., postcode: _Optional[str] = ...,
                 zip_plus4: _Optional[int] = ..., phone: _Optional[str] = ...) -> None: ...


class CCDDBAppDetailCommon(_message.Message):
    __slots__: List[str] = ["app_type", "appid", "community_visible_stats", "content_descriptorids", "demo",
                            "friendly_name", "has_adult_content", "has_adult_content_sex", "has_adult_content_violence",
                            "icon", "is_visible_in_steam_china", "media", "name", "propagation", "tool"]
    APPID_FIELD_NUMBER: _ClassVar[int]
    APP_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_VISIBLE_STATS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DESCRIPTORIDS_FIELD_NUMBER: _ClassVar[int]
    DEMO_FIELD_NUMBER: _ClassVar[int]
    FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    HAS_ADULT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    HAS_ADULT_CONTENT_SEX_FIELD_NUMBER: _ClassVar[int]
    HAS_ADULT_CONTENT_VIOLENCE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    IS_VISIBLE_IN_STEAM_CHINA_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPAGATION_FIELD_NUMBER: _ClassVar[int]
    TOOL_FIELD_NUMBER: _ClassVar[int]
    app_type: int
    appid: int
    community_visible_stats: bool
    content_descriptorids: _containers.RepeatedScalarFieldContainer[int]
    demo: bool
    friendly_name: str
    has_adult_content: bool
    has_adult_content_sex: bool
    has_adult_content_violence: bool
    icon: str
    is_visible_in_steam_china: bool
    media: bool
    name: str
    propagation: str
    tool: bool

    def __init__(self, appid: _Optional[int] = ..., name: _Optional[str] = ..., icon: _Optional[str] = ...,
                 tool: bool = ..., demo: bool = ..., media: bool = ..., community_visible_stats: bool = ...,
                 friendly_name: _Optional[str] = ..., propagation: _Optional[str] = ..., has_adult_content: bool = ...,
                 is_visible_in_steam_china: bool = ..., app_type: _Optional[int] = ...,
                 has_adult_content_sex: bool = ..., has_adult_content_violence: bool = ...,
                 content_descriptorids: _Optional[_Iterable[int]] = ...) -> None: ...


class CClanEventData(_message.Message):
    __slots__: List[str] = ["announcement_body", "appid", "broadcaster_accountid", "build_branch", "build_id",
                            "clan_steamid", "comment_count", "creator_steamid", "event_name", "event_notes",
                            "event_type", "featured_app_tagid", "follower_count", "forum_topic_id", "gid", "hidden",
                            "ignore_count", "jsondata", "last_update_steamid", "news_post_gid", "published",
                            "referenced_appids", "rtime32_end_time", "rtime32_last_modified", "rtime32_start_time",
                            "rtime32_visibility_end", "rtime32_visibility_start", "rtime_mod_reviewed",
                            "server_address", "server_password"]
    ANNOUNCEMENT_BODY_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    BROADCASTER_ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    BUILD_BRANCH_FIELD_NUMBER: _ClassVar[int]
    BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    CLAN_STEAMID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATOR_STEAMID_FIELD_NUMBER: _ClassVar[int]
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_NOTES_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FEATURED_APP_TAGID_FIELD_NUMBER: _ClassVar[int]
    FOLLOWER_COUNT_FIELD_NUMBER: _ClassVar[int]
    FORUM_TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    IGNORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    JSONDATA_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_STEAMID_FIELD_NUMBER: _ClassVar[int]
    NEWS_POST_GID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    REFERENCED_APPIDS_FIELD_NUMBER: _ClassVar[int]
    RTIME32_END_TIME_FIELD_NUMBER: _ClassVar[int]
    RTIME32_LAST_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    RTIME32_START_TIME_FIELD_NUMBER: _ClassVar[int]
    RTIME32_VISIBILITY_END_FIELD_NUMBER: _ClassVar[int]
    RTIME32_VISIBILITY_START_FIELD_NUMBER: _ClassVar[int]
    RTIME_MOD_REVIEWED_FIELD_NUMBER: _ClassVar[int]
    SERVER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SERVER_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    announcement_body: CCommunity_ClanAnnouncementInfo
    appid: int
    broadcaster_accountid: int
    build_branch: str
    build_id: int
    clan_steamid: int
    comment_count: int
    creator_steamid: int
    event_name: str
    event_notes: str
    event_type: EProtoClanEventType
    featured_app_tagid: int
    follower_count: int
    forum_topic_id: int
    gid: int
    hidden: bool
    ignore_count: int
    jsondata: str
    last_update_steamid: int
    news_post_gid: int
    published: bool
    referenced_appids: _containers.RepeatedScalarFieldContainer[int]
    rtime32_end_time: int
    rtime32_last_modified: int
    rtime32_start_time: int
    rtime32_visibility_end: int
    rtime32_visibility_start: int
    rtime_mod_reviewed: int
    server_address: str
    server_password: str

    def __init__(self, gid: _Optional[int] = ..., clan_steamid: _Optional[int] = ..., event_name: _Optional[str] = ...,
                 event_type: _Optional[_Union[EProtoClanEventType, str]] = ..., appid: _Optional[int] = ...,
                 server_address: _Optional[str] = ..., server_password: _Optional[str] = ...,
                 rtime32_start_time: _Optional[int] = ..., rtime32_end_time: _Optional[int] = ...,
                 comment_count: _Optional[int] = ..., creator_steamid: _Optional[int] = ...,
                 last_update_steamid: _Optional[int] = ..., event_notes: _Optional[str] = ...,
                 jsondata: _Optional[str] = ...,
                 announcement_body: _Optional[_Union[CCommunity_ClanAnnouncementInfo, _Mapping]] = ...,
                 published: bool = ..., hidden: bool = ..., rtime32_visibility_start: _Optional[int] = ...,
                 rtime32_visibility_end: _Optional[int] = ..., broadcaster_accountid: _Optional[int] = ...,
                 follower_count: _Optional[int] = ..., ignore_count: _Optional[int] = ...,
                 forum_topic_id: _Optional[int] = ..., rtime32_last_modified: _Optional[int] = ...,
                 news_post_gid: _Optional[int] = ..., rtime_mod_reviewed: _Optional[int] = ...,
                 featured_app_tagid: _Optional[int] = ..., referenced_appids: _Optional[_Iterable[int]] = ...,
                 build_id: _Optional[int] = ..., build_branch: _Optional[str] = ...) -> None: ...


class CClanEventUserNewsTuple(_message.Message):
    __slots__: List[str] = ["announcement_gid", "appid", "clamp_range_slot", "clanid", "event_gid", "priority_score",
                            "rtime32_last_modified", "rtime_end", "rtime_start", "type"]
    ANNOUNCEMENT_GID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    CLAMP_RANGE_SLOT_FIELD_NUMBER: _ClassVar[int]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    EVENT_GID_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_SCORE_FIELD_NUMBER: _ClassVar[int]
    RTIME32_LAST_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    RTIME_END_FIELD_NUMBER: _ClassVar[int]
    RTIME_START_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    announcement_gid: int
    appid: int
    clamp_range_slot: int
    clanid: int
    event_gid: int
    priority_score: int
    rtime32_last_modified: int
    rtime_end: int
    rtime_start: int
    type: int

    def __init__(self, clanid: _Optional[int] = ..., event_gid: _Optional[int] = ...,
                 announcement_gid: _Optional[int] = ..., rtime_start: _Optional[int] = ...,
                 rtime_end: _Optional[int] = ..., priority_score: _Optional[int] = ..., type: _Optional[int] = ...,
                 clamp_range_slot: _Optional[int] = ..., appid: _Optional[int] = ...,
                 rtime32_last_modified: _Optional[int] = ...) -> None: ...


class CClanMatchEventByRange(_message.Message):
    __slots__: List[str] = ["events", "qualified", "rtime_after", "rtime_before"]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    QUALIFIED_FIELD_NUMBER: _ClassVar[int]
    RTIME_AFTER_FIELD_NUMBER: _ClassVar[int]
    RTIME_BEFORE_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[CClanEventUserNewsTuple]
    qualified: int
    rtime_after: int
    rtime_before: int

    def __init__(self, rtime_before: _Optional[int] = ..., rtime_after: _Optional[int] = ...,
                 qualified: _Optional[int] = ...,
                 events: _Optional[_Iterable[_Union[CClanEventUserNewsTuple, _Mapping]]] = ...) -> None: ...


class CCommunity_ClanAnnouncementInfo(_message.Message):
    __slots__: List[str] = ["ban_check_result", "banned", "body", "clanid", "commentcount", "event_gid",
                            "forum_topic_id", "gid", "headline", "hidden", "language", "posterid", "posttime", "tags",
                            "updatetime", "votedowncount", "voteupcount"]
    BANNED_FIELD_NUMBER: _ClassVar[int]
    BAN_CHECK_RESULT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    COMMENTCOUNT_FIELD_NUMBER: _ClassVar[int]
    EVENT_GID_FIELD_NUMBER: _ClassVar[int]
    FORUM_TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    POSTERID_FIELD_NUMBER: _ClassVar[int]
    POSTTIME_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    UPDATETIME_FIELD_NUMBER: _ClassVar[int]
    VOTEDOWNCOUNT_FIELD_NUMBER: _ClassVar[int]
    VOTEUPCOUNT_FIELD_NUMBER: _ClassVar[int]
    ban_check_result: EBanContentCheckResult
    banned: bool
    body: str
    clanid: int
    commentcount: int
    event_gid: int
    forum_topic_id: int
    gid: int
    headline: str
    hidden: bool
    language: int
    posterid: int
    posttime: int
    tags: _containers.RepeatedScalarFieldContainer[str]
    updatetime: int
    votedowncount: int
    voteupcount: int

    def __init__(self, gid: _Optional[int] = ..., clanid: _Optional[int] = ..., posterid: _Optional[int] = ...,
                 headline: _Optional[str] = ..., posttime: _Optional[int] = ..., updatetime: _Optional[int] = ...,
                 body: _Optional[str] = ..., commentcount: _Optional[int] = ..., tags: _Optional[_Iterable[str]] = ...,
                 language: _Optional[int] = ..., hidden: bool = ..., forum_topic_id: _Optional[int] = ...,
                 event_gid: _Optional[int] = ..., voteupcount: _Optional[int] = ...,
                 votedowncount: _Optional[int] = ...,
                 ban_check_result: _Optional[_Union[EBanContentCheckResult, str]] = ...,
                 banned: bool = ...) -> None: ...


class CCuratorPreferences(_message.Message):
    __slots__: List[str] = ["adult_content_sex", "adult_content_violence", "discussion_url", "platform_linux",
                            "platform_mac", "platform_windows", "show_broadcast", "supported_languages",
                            "tagids_curated", "tagids_filtered", "timestamp_updated", "vr_content", "website_title",
                            "website_url"]
    ADULT_CONTENT_SEX_FIELD_NUMBER: _ClassVar[int]
    ADULT_CONTENT_VIOLENCE_FIELD_NUMBER: _ClassVar[int]
    DISCUSSION_URL_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_LINUX_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_MAC_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_WINDOWS_FIELD_NUMBER: _ClassVar[int]
    SHOW_BROADCAST_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    TAGIDS_CURATED_FIELD_NUMBER: _ClassVar[int]
    TAGIDS_FILTERED_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_UPDATED_FIELD_NUMBER: _ClassVar[int]
    VR_CONTENT_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_TITLE_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_URL_FIELD_NUMBER: _ClassVar[int]
    adult_content_sex: bool
    adult_content_violence: bool
    discussion_url: str
    platform_linux: bool
    platform_mac: bool
    platform_windows: bool
    show_broadcast: bool
    supported_languages: int
    tagids_curated: _containers.RepeatedScalarFieldContainer[int]
    tagids_filtered: _containers.RepeatedScalarFieldContainer[int]
    timestamp_updated: int
    vr_content: bool
    website_title: str
    website_url: str

    def __init__(self, supported_languages: _Optional[int] = ..., platform_windows: bool = ...,
                 platform_mac: bool = ..., platform_linux: bool = ..., vr_content: bool = ...,
                 adult_content_violence: bool = ..., adult_content_sex: bool = ...,
                 timestamp_updated: _Optional[int] = ..., tagids_curated: _Optional[_Iterable[int]] = ...,
                 tagids_filtered: _Optional[_Iterable[int]] = ..., website_title: _Optional[str] = ...,
                 website_url: _Optional[str] = ..., discussion_url: _Optional[str] = ...,
                 show_broadcast: bool = ...) -> None: ...


class CLocalizationToken(_message.Message):
    __slots__: List[str] = ["language", "localized_string"]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    LOCALIZED_STRING_FIELD_NUMBER: _ClassVar[int]
    language: int
    localized_string: str

    def __init__(self, language: _Optional[int] = ..., localized_string: _Optional[str] = ...) -> None: ...


class CMsgAppRights(_message.Message):
    __slots__: List[str] = ["broadcast_live", "download", "economy_support", "economy_support_supervisor", "edit_info",
                            "edit_marketing", "edit_store_display_content", "generate_cdkeys", "manage_cdkeys",
                            "manage_ceg", "manage_pricing", "manage_signing", "publish", "upload_cdkeys",
                            "view_error_data", "view_financials", "view_marketing_traffic"]
    BROADCAST_LIVE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    ECONOMY_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    ECONOMY_SUPPORT_SUPERVISOR_FIELD_NUMBER: _ClassVar[int]
    EDIT_INFO_FIELD_NUMBER: _ClassVar[int]
    EDIT_MARKETING_FIELD_NUMBER: _ClassVar[int]
    EDIT_STORE_DISPLAY_CONTENT_FIELD_NUMBER: _ClassVar[int]
    GENERATE_CDKEYS_FIELD_NUMBER: _ClassVar[int]
    MANAGE_CDKEYS_FIELD_NUMBER: _ClassVar[int]
    MANAGE_CEG_FIELD_NUMBER: _ClassVar[int]
    MANAGE_PRICING_FIELD_NUMBER: _ClassVar[int]
    MANAGE_SIGNING_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_CDKEYS_FIELD_NUMBER: _ClassVar[int]
    VIEW_ERROR_DATA_FIELD_NUMBER: _ClassVar[int]
    VIEW_FINANCIALS_FIELD_NUMBER: _ClassVar[int]
    VIEW_MARKETING_TRAFFIC_FIELD_NUMBER: _ClassVar[int]
    broadcast_live: bool
    download: bool
    economy_support: bool
    economy_support_supervisor: bool
    edit_info: bool
    edit_marketing: bool
    edit_store_display_content: bool
    generate_cdkeys: bool
    manage_cdkeys: bool
    manage_ceg: bool
    manage_pricing: bool
    manage_signing: bool
    publish: bool
    upload_cdkeys: bool
    view_error_data: bool
    view_financials: bool
    view_marketing_traffic: bool

    def __init__(self, edit_info: bool = ..., publish: bool = ..., view_error_data: bool = ..., download: bool = ...,
                 upload_cdkeys: bool = ..., generate_cdkeys: bool = ..., view_financials: bool = ...,
                 manage_ceg: bool = ..., manage_signing: bool = ..., manage_cdkeys: bool = ...,
                 edit_marketing: bool = ..., economy_support: bool = ..., economy_support_supervisor: bool = ...,
                 manage_pricing: bool = ..., broadcast_live: bool = ..., view_marketing_traffic: bool = ...,
                 edit_store_display_content: bool = ...) -> None: ...


class CMsgAuthTicket(_message.Message):
    __slots__: List[str] = ["eresult", "estate", "gameid", "h_steam_pipe", "server_secret", "steamid", "ticket",
                            "ticket_crc"]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    ESTATE_FIELD_NUMBER: _ClassVar[int]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    H_STEAM_PIPE_FIELD_NUMBER: _ClassVar[int]
    SERVER_SECRET_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    TICKET_CRC_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    estate: int
    gameid: int
    h_steam_pipe: int
    server_secret: bytes
    steamid: int
    ticket: bytes
    ticket_crc: int

    def __init__(self, estate: _Optional[int] = ..., eresult: _Optional[int] = ..., steamid: _Optional[int] = ...,
                 gameid: _Optional[int] = ..., h_steam_pipe: _Optional[int] = ..., ticket_crc: _Optional[int] = ...,
                 ticket: _Optional[bytes] = ..., server_secret: _Optional[bytes] = ...) -> None: ...


class CMsgGCRoutingProtoBufHeader(_message.Message):
    __slots__: List[str] = ["dst_gc_dir_index", "dst_gcid_queue"]
    DST_GCID_QUEUE_FIELD_NUMBER: _ClassVar[int]
    DST_GC_DIR_INDEX_FIELD_NUMBER: _ClassVar[int]
    dst_gc_dir_index: int
    dst_gcid_queue: int

    def __init__(self, dst_gcid_queue: _Optional[int] = ..., dst_gc_dir_index: _Optional[int] = ...) -> None: ...


class CMsgIPAddress(_message.Message):
    __slots__: List[str] = ["v4", "v6"]
    V4_FIELD_NUMBER: _ClassVar[int]
    V6_FIELD_NUMBER: _ClassVar[int]
    v4: int
    v6: bytes

    def __init__(self, v4: _Optional[int] = ..., v6: _Optional[bytes] = ...) -> None: ...


class CMsgIPAddressBucket(_message.Message):
    __slots__: List[str] = ["bucket", "original_ip_address"]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    bucket: int
    original_ip_address: CMsgIPAddress

    def __init__(self, original_ip_address: _Optional[_Union[CMsgIPAddress, _Mapping]] = ...,
                 bucket: _Optional[int] = ...) -> None: ...


class CMsgKeyValuePair(_message.Message):
    __slots__: List[str] = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str

    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...


class CMsgKeyValueSet(_message.Message):
    __slots__: List[str] = ["pairs"]
    PAIRS_FIELD_NUMBER: _ClassVar[int]
    pairs: _containers.RepeatedCompositeFieldContainer[CMsgKeyValuePair]

    def __init__(self, pairs: _Optional[_Iterable[_Union[CMsgKeyValuePair, _Mapping]]] = ...) -> None: ...


class CMsgMulti(_message.Message):
    __slots__: List[str] = ["message_body", "size_unzipped"]
    MESSAGE_BODY_FIELD_NUMBER: _ClassVar[int]
    SIZE_UNZIPPED_FIELD_NUMBER: _ClassVar[int]
    message_body: bytes
    size_unzipped: int

    def __init__(self, size_unzipped: _Optional[int] = ..., message_body: _Optional[bytes] = ...) -> None: ...


class CMsgProtoBufHeader(_message.Message):
    __slots__: List[str] = ["admin_spoofing_user", "auth_account_flags", "client_sessionid", "cm_sysid", "debug_source",
                            "debug_source_string_index", "eresult", "error_message", "forward_to_sysid", "ip", "ip_v6",
                            "is_from_external_source", "jobid_source", "jobid_target", "launcher_type", "messageid",
                            "publisher_group_id", "realm", "routing_appid", "routing_gc", "seq_num", "steamid", "sysid",
                            "target_job_name", "timeout_ms", "token_id", "token_source", "trace_tag", "transport_error",
                            "webapi_key_id"]
    ADMIN_SPOOFING_USER_FIELD_NUMBER: _ClassVar[int]
    AUTH_ACCOUNT_FLAGS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SESSIONID_FIELD_NUMBER: _ClassVar[int]
    CM_SYSID_FIELD_NUMBER: _ClassVar[int]
    DEBUG_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DEBUG_SOURCE_STRING_INDEX_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FORWARD_TO_SYSID_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    IP_V6_FIELD_NUMBER: _ClassVar[int]
    IS_FROM_EXTERNAL_SOURCE_FIELD_NUMBER: _ClassVar[int]
    JOBID_SOURCE_FIELD_NUMBER: _ClassVar[int]
    JOBID_TARGET_FIELD_NUMBER: _ClassVar[int]
    LAUNCHER_TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGEID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    REALM_FIELD_NUMBER: _ClassVar[int]
    ROUTING_APPID_FIELD_NUMBER: _ClassVar[int]
    ROUTING_GC_FIELD_NUMBER: _ClassVar[int]
    SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    SYSID_FIELD_NUMBER: _ClassVar[int]
    TARGET_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_SOURCE_FIELD_NUMBER: _ClassVar[int]
    TRACE_TAG_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_ERROR_FIELD_NUMBER: _ClassVar[int]
    WEBAPI_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    admin_spoofing_user: bool
    auth_account_flags: int
    client_sessionid: int
    cm_sysid: int
    debug_source: str
    debug_source_string_index: int
    eresult: int
    error_message: str
    forward_to_sysid: _containers.RepeatedScalarFieldContainer[int]
    ip: int
    ip_v6: bytes
    is_from_external_source: bool
    jobid_source: int
    jobid_target: int
    launcher_type: int
    messageid: int
    publisher_group_id: int
    realm: int
    routing_appid: int
    routing_gc: CMsgGCRoutingProtoBufHeader
    seq_num: int
    steamid: int
    sysid: int
    target_job_name: str
    timeout_ms: int
    token_id: int
    token_source: int
    trace_tag: int
    transport_error: int
    webapi_key_id: int

    def __init__(self, steamid: _Optional[int] = ..., client_sessionid: _Optional[int] = ...,
                 routing_appid: _Optional[int] = ..., jobid_source: _Optional[int] = ...,
                 jobid_target: _Optional[int] = ..., target_job_name: _Optional[str] = ...,
                 seq_num: _Optional[int] = ..., eresult: _Optional[int] = ..., error_message: _Optional[str] = ...,
                 auth_account_flags: _Optional[int] = ..., token_source: _Optional[int] = ...,
                 admin_spoofing_user: bool = ..., transport_error: _Optional[int] = ...,
                 messageid: _Optional[int] = ..., publisher_group_id: _Optional[int] = ..., sysid: _Optional[int] = ...,
                 trace_tag: _Optional[int] = ..., webapi_key_id: _Optional[int] = ...,
                 is_from_external_source: bool = ..., forward_to_sysid: _Optional[_Iterable[int]] = ...,
                 cm_sysid: _Optional[int] = ..., launcher_type: _Optional[int] = ..., realm: _Optional[int] = ...,
                 timeout_ms: _Optional[int] = ..., debug_source: _Optional[str] = ...,
                 debug_source_string_index: _Optional[int] = ..., token_id: _Optional[int] = ...,
                 routing_gc: _Optional[_Union[CMsgGCRoutingProtoBufHeader, _Mapping]] = ..., ip: _Optional[int] = ...,
                 ip_v6: _Optional[bytes] = ...) -> None: ...


class CMsgProtobufWrapped(_message.Message):
    __slots__: List[str] = ["message_body"]
    MESSAGE_BODY_FIELD_NUMBER: _ClassVar[int]
    message_body: bytes

    def __init__(self, message_body: _Optional[bytes] = ...) -> None: ...


class CPackageReservationStatus(_message.Message):
    __slots__: List[str] = ["expired", "packageid", "queue_position", "reservation_country_code", "reservation_state",
                            "time_expires", "time_reserved", "total_queue_size"]
    EXPIRED_FIELD_NUMBER: _ClassVar[int]
    PACKAGEID_FIELD_NUMBER: _ClassVar[int]
    QUEUE_POSITION_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_STATE_FIELD_NUMBER: _ClassVar[int]
    TIME_EXPIRES_FIELD_NUMBER: _ClassVar[int]
    TIME_RESERVED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_QUEUE_SIZE_FIELD_NUMBER: _ClassVar[int]
    expired: bool
    packageid: int
    queue_position: int
    reservation_country_code: str
    reservation_state: int
    time_expires: int
    time_reserved: int
    total_queue_size: int

    def __init__(self, packageid: _Optional[int] = ..., reservation_state: _Optional[int] = ...,
                 queue_position: _Optional[int] = ..., total_queue_size: _Optional[int] = ...,
                 reservation_country_code: _Optional[str] = ..., expired: bool = ...,
                 time_expires: _Optional[int] = ..., time_reserved: _Optional[int] = ...) -> None: ...


class EBanContentCheckResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__: List[str] = []


class EProtoClanEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__: List[str] = []


class PartnerEventNotificationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__: List[str] = []
