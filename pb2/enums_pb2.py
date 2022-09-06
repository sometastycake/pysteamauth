# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: enums.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message  # noqa
from google.protobuf import reflection as _reflection  # noqa
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper


# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from . import steammessages_base_pb2 as steammessages__base__pb2  # noqa


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x65nums.proto\x1a\x18steammessages_base.proto*\x80\n\n\x17\x45PublishedFileQueryType\x12)\n%k_PublishedFileQueryType_RankedByVote\x10\x00\x12\x34\n0k_PublishedFileQueryType_RankedByPublicationDate\x10\x01\x12\x42\n>k_PublishedFileQueryType_AcceptedForGameRankedByAcceptanceDate\x10\x02\x12*\n&k_PublishedFileQueryType_RankedByTrend\x10\x03\x12\x46\nBk_PublishedFileQueryType_FavoritedByFriendsRankedByPublicationDate\x10\x04\x12\x44\n@k_PublishedFileQueryType_CreatedByFriendsRankedByPublicationDate\x10\x05\x12\x35\n1k_PublishedFileQueryType_RankedByNumTimesReported\x10\x06\x12J\nFk_PublishedFileQueryType_CreatedByFollowedUsersRankedByPublicationDate\x10\x07\x12(\n$k_PublishedFileQueryType_NotYetRated\x10\x08\x12=\n9k_PublishedFileQueryType_RankedByTotalUniqueSubscriptions\x10\t\x12\x32\n.k_PublishedFileQueryType_RankedByTotalVotesAsc\x10\n\x12,\n(k_PublishedFileQueryType_RankedByVotesUp\x10\x0b\x12/\n+k_PublishedFileQueryType_RankedByTextSearch\x10\x0c\x12\x32\n.k_PublishedFileQueryType_RankedByPlaytimeTrend\x10\r\x12\x32\n.k_PublishedFileQueryType_RankedByTotalPlaytime\x10\x0e\x12\x39\n5k_PublishedFileQueryType_RankedByAveragePlaytimeTrend\x10\x0f\x12<\n8k_PublishedFileQueryType_RankedByLifetimeAveragePlaytime\x10\x10\x12:\n6k_PublishedFileQueryType_RankedByPlaytimeSessionsTrend\x10\x11\x12=\n9k_PublishedFileQueryType_RankedByLifetimePlaytimeSessions\x10\x12\x12?\n;k_PublishedFileQueryType_RankedByInappropriateContentRating\x10\x13\x12\x34\n0k_PublishedFileQueryType_RankedByBanContentCheck\x10\x14\x12\x34\n0k_PublishedFileQueryType_RankedByLastUpdatedDate\x10\x15*\xbc\x01\n#EPublishedFileInappropriateProvider\x12\x31\n-k_EPublishedFileInappropriateProvider_Invalid\x10\x00\x12\x30\n,k_EPublishedFileInappropriateProvider_Google\x10\x01\x12\x30\n,k_EPublishedFileInappropriateProvider_Amazon\x10\x02*\xd5\x02\n!EPublishedFileInappropriateResult\x12\x32\n.k_EPublishedFileInappropriateResult_NotScanned\x10\x00\x12\x34\n0k_EPublishedFileInappropriateResult_VeryUnlikely\x10\x01\x12\x30\n,k_EPublishedFileInappropriateResult_Unlikely\x10\x1e\x12\x30\n,k_EPublishedFileInappropriateResult_Possible\x10\x32\x12.\n*k_EPublishedFileInappropriateResult_Likely\x10K\x12\x32\n.k_EPublishedFileInappropriateResult_VeryLikely\x10\x64*\xb1\x03\n\x11\x45PersonaStateFlag\x12\'\n#k_EPersonaStateFlag_HasRichPresence\x10\x01\x12&\n\"k_EPersonaStateFlag_InJoinableGame\x10\x02\x12\x1e\n\x1ak_EPersonaStateFlag_Golden\x10\x04\x12*\n&k_EPersonaStateFlag_RemotePlayTogether\x10\x08\x12&\n!k_EPersonaStateFlag_ClientTypeWeb\x10\x80\x02\x12)\n$k_EPersonaStateFlag_ClientTypeMobile\x10\x80\x04\x12*\n%k_EPersonaStateFlag_ClientTypeTenfoot\x10\x80\x08\x12%\n k_EPersonaStateFlag_ClientTypeVR\x10\x80\x10\x12*\n%k_EPersonaStateFlag_LaunchTypeGamepad\x10\x80 \x12-\n(k_EPersonaStateFlag_LaunchTypeCompatTool\x10\x80@*\xa7\x01\n\x15\x45\x43ontentCheckProvider\x12#\n\x1fk_EContentCheckProvider_Invalid\x10\x00\x12\"\n\x1ek_EContentCheckProvider_Google\x10\x01\x12\"\n\x1ek_EContentCheckProvider_Amazon\x10\x02\x12!\n\x1dk_EContentCheckProvider_Local\x10\x03*\xec\x08\n\x19\x45ProfileCustomizationType\x12&\n\"k_EProfileCustomizationTypeInvalid\x10\x00\x12\x36\n2k_EProfileCustomizationTypeRareAchievementShowcase\x10\x01\x12,\n(k_EProfileCustomizationTypeGameCollector\x10\x02\x12+\n\'k_EProfileCustomizationTypeItemShowcase\x10\x03\x12,\n(k_EProfileCustomizationTypeTradeShowcase\x10\x04\x12%\n!k_EProfileCustomizationTypeBadges\x10\x05\x12+\n\'k_EProfileCustomizationTypeFavoriteGame\x10\x06\x12\x31\n-k_EProfileCustomizationTypeScreenshotShowcase\x10\x07\x12)\n%k_EProfileCustomizationTypeCustomText\x10\x08\x12,\n(k_EProfileCustomizationTypeFavoriteGroup\x10\t\x12-\n)k_EProfileCustomizationTypeRecommendation\x10\n\x12+\n\'k_EProfileCustomizationTypeWorkshopItem\x10\x0b\x12)\n%k_EProfileCustomizationTypeMyWorkshop\x10\x0c\x12.\n*k_EProfileCustomizationTypeArtworkShowcase\x10\r\x12,\n(k_EProfileCustomizationTypeVideoShowcase\x10\x0e\x12%\n!k_EProfileCustomizationTypeGuides\x10\x0f\x12\'\n#k_EProfileCustomizationTypeMyGuides\x10\x10\x12+\n\'k_EProfileCustomizationTypeAchievements\x10\x11\x12)\n%k_EProfileCustomizationTypeGreenlight\x10\x12\x12+\n\'k_EProfileCustomizationTypeMyGreenlight\x10\x13\x12%\n!k_EProfileCustomizationTypeSalien\x10\x14\x12\x35\n1k_EProfileCustomizationTypeLoyaltyRewardReactions\x10\x15\x12\x34\n0k_EProfileCustomizationTypeSingleArtworkShowcase\x10\x16\x12\x38\n4k_EProfileCustomizationTypeAchievementsCompletionist\x10\x17*\xc8\x01\n\x1b\x45PublishedFileStorageSystem\x12(\n$k_EPublishedFileStorageSystemInvalid\x10\x00\x12,\n(k_EPublishedFileStorageSystemLegacyCloud\x10\x01\x12&\n\"k_EPublishedFileStorageSystemDepot\x10\x02\x12)\n%k_EPublishedFileStorageSystemUGCCloud\x10\x03*\x97\x01\n\x19\x45\x43loudStoragePersistState\x12(\n$k_ECloudStoragePersistStatePersisted\x10\x00\x12(\n$k_ECloudStoragePersistStateForgotten\x10\x01\x12&\n\"k_ECloudStoragePersistStateDeleted\x10\x02*\xe8\x01\n\x12\x45SDCardFormatStage\x12 \n\x1ck_ESDCardFormatStage_Invalid\x10\x00\x12!\n\x1dk_ESDCardFormatStage_Starting\x10\x01\x12 \n\x1ck_ESDCardFormatStage_Testing\x10\x02\x12!\n\x1dk_ESDCardFormatStage_Rescuing\x10\x03\x12#\n\x1fk_ESDCardFormatStage_Formatting\x10\x04\x12#\n\x1fk_ESDCardFormatStage_Finalizing\x10\x05*\x84\x01\n\x15\x45SystemFanControlMode\x12\"\n\x1ek_SystemFanControlMode_Invalid\x10\x00\x12#\n\x1fk_SystemFanControlMode_Disabled\x10\x01\x12\"\n\x1ek_SystemFanControlMode_Default\x10\x02*\x81\x01\n\rEColorProfile\x12\x1b\n\x17k_EColorProfile_Invalid\x10\x00\x12\x1a\n\x16k_EColorProfile_Native\x10\x01\x12\x1c\n\x18k_EColorProfile_Standard\x10\x02\x12\x19\n\x15k_EColorProfile_Vivid\x10\x03*\xc0\x03\n\x14\x45\x42luetoothDeviceType\x12!\n\x1dk_BluetoothDeviceType_Invalid\x10\x00\x12!\n\x1dk_BluetoothDeviceType_Unknown\x10\x01\x12\x1f\n\x1bk_BluetoothDeviceType_Phone\x10\x02\x12\"\n\x1ek_BluetoothDeviceType_Computer\x10\x03\x12!\n\x1dk_BluetoothDeviceType_Headset\x10\x04\x12$\n k_BluetoothDeviceType_Headphones\x10\x05\x12\"\n\x1ek_BluetoothDeviceType_Speakers\x10\x06\x12$\n k_BluetoothDeviceType_OtherAudio\x10\x07\x12\x1f\n\x1bk_BluetoothDeviceType_Mouse\x10\x08\x12\"\n\x1ek_BluetoothDeviceType_Joystick\x10\t\x12!\n\x1dk_BluetoothDeviceType_Gamepad\x10\n\x12\"\n\x1ek_BluetoothDeviceType_Keyboard\x10\x0b*\x80\x01\n\x15\x45SystemAudioDirection\x12\"\n\x1ek_SystemAudioDirection_Invalid\x10\x00\x12 \n\x1ck_SystemAudioDirection_Input\x10\x01\x12!\n\x1dk_SystemAudioDirection_Output\x10\x02*\xf1\x02\n\x13\x45SystemAudioChannel\x12 \n\x1ck_SystemAudioChannel_Invalid\x10\x00\x12#\n\x1fk_SystemAudioChannel_Aggregated\x10\x01\x12\"\n\x1ek_SystemAudioChannel_FrontLeft\x10\x02\x12#\n\x1fk_SystemAudioChannel_FrontRight\x10\x03\x12\x1c\n\x18k_SystemAudioChannel_LFE\x10\x04\x12!\n\x1dk_SystemAudioChannel_BackLeft\x10\x05\x12\"\n\x1ek_SystemAudioChannel_BackRight\x10\x06\x12$\n k_SystemAudioChannel_FrontCenter\x10\x07\x12 \n\x1ck_SystemAudioChannel_Unknown\x10\x08\x12\x1d\n\x19k_SystemAudioChannel_Mono\x10\t*\xc9\x01\n\x14\x45SystemAudioPortType\x12!\n\x1dk_SystemAudioPortType_Invalid\x10\x00\x12!\n\x1dk_SystemAudioPortType_Unknown\x10\x01\x12\"\n\x1ek_SystemAudioPortType_Audio32f\x10\x02\x12 \n\x1ck_SystemAudioPortType_Midi8b\x10\x03\x12%\n!k_SystemAudioPortType_Video32RGBA\x10\x04*\x90\x01\n\x19\x45SystemAudioPortDirection\x12&\n\"k_SystemAudioPortDirection_Invalid\x10\x00\x12$\n k_SystemAudioPortDirection_Input\x10\x01\x12%\n!k_SystemAudioPortDirection_Output\x10\x02*\x83\x01\n\x13\x45SystemServiceState\x12%\n!k_ESystemServiceState_Unavailable\x10\x00\x12\"\n\x1ek_ESystemServiceState_Disabled\x10\x01\x12!\n\x1dk_ESystemServiceState_Enabled\x10\x02*\xe1\x01\n\x19\x45GraphicsPerfOverlayLevel\x12&\n\"k_EGraphicsPerfOverlayLevel_Hidden\x10\x00\x12%\n!k_EGraphicsPerfOverlayLevel_Basic\x10\x01\x12&\n\"k_EGraphicsPerfOverlayLevel_Medium\x10\x02\x12$\n k_EGraphicsPerfOverlayLevel_Full\x10\x03\x12\'\n#k_EGraphicsPerfOverlayLevel_Minimal\x10\x04*\xe5\x01\n\x14\x45GPUPerformanceLevel\x12\"\n\x1ek_EGPUPerformanceLevel_Invalid\x10\x00\x12\x1f\n\x1bk_EGPUPerformanceLevel_Auto\x10\x01\x12!\n\x1dk_EGPUPerformanceLevel_Manual\x10\x02\x12\x1e\n\x1ak_EGPUPerformanceLevel_Low\x10\x03\x12\x1f\n\x1bk_EGPUPerformanceLevel_High\x10\x04\x12$\n k_EGPUPerformanceLevel_Profiling\x10\x05*\xbb\x01\n\x0e\x45ScalingFilter\x12\x1c\n\x18k_EScalingFilter_Invalid\x10\x00\x12\x18\n\x14k_EScalingFilter_FSR\x10\x01\x12\x1c\n\x18k_EScalingFilter_Nearest\x10\x02\x12\x1c\n\x18k_EScalingFilter_Integer\x10\x03\x12\x1b\n\x17k_EScalingFilter_Linear\x10\x04\x12\x18\n\x14k_EScalingFilter_NIS\x10\x05*|\n\x0c\x45\x43PUGovernor\x12\x1a\n\x16k_ECPUGovernor_Invalid\x10\x00\x12\x17\n\x13k_ECPUGovernor_Perf\x10\x01\x12\x1c\n\x18k_ECPUGovernor_Powersave\x10\x02\x12\x19\n\x15k_ECPUGovernor_Manual\x10\x03*\xe2\x01\n\x0c\x45UpdaterType\x12\x1a\n\x16k_EUpdaterType_Invalid\x10\x00\x12\x19\n\x15k_EUpdaterType_Client\x10\x01\x12\x15\n\x11k_EUpdaterType_OS\x10\x02\x12\x17\n\x13k_EUpdaterType_BIOS\x10\x03\x12\x1d\n\x19k_EUpdaterType_Aggregated\x10\x04\x12\x18\n\x14k_EUpdaterType_Test1\x10\x05\x12\x18\n\x14k_EUpdaterType_Test2\x10\x06\x12\x18\n\x14k_EUpdaterType_Dummy\x10\x07*\xf9\x01\n\rEUpdaterState\x12\x1b\n\x17k_EUpdaterState_Invalid\x10\x00\x12\x1c\n\x18k_EUpdaterState_UpToDate\x10\x02\x12\x1c\n\x18k_EUpdaterState_Checking\x10\x03\x12\x1d\n\x19k_EUpdaterState_Available\x10\x04\x12\x1c\n\x18k_EUpdaterState_Applying\x10\x05\x12(\n$k_EUpdaterState_ClientRestartPending\x10\x06\x12(\n$k_EUpdaterState_SystemRestartPending\x10\x07*\xe1\x01\n\x18\x45StorageBlockContentType\x12&\n\"k_EStorageBlockContentType_Invalid\x10\x00\x12&\n\"k_EStorageBlockContentType_Unknown\x10\x01\x12)\n%k_EStorageBlockContentType_FileSystem\x10\x02\x12%\n!k_EStorageBlockContentType_Crypto\x10\x03\x12#\n\x1fk_EStorageBlockContentType_Raid\x10\x04*\xc3\x01\n\x1b\x45StorageBlockFileSystemType\x12)\n%k_EStorageBlockFileSystemType_Invalid\x10\x00\x12)\n%k_EStorageBlockFileSystemType_Unknown\x10\x01\x12&\n\"k_EStorageBlockFileSystemType_VFat\x10\x02\x12&\n\"k_EStorageBlockFileSystemType_Ext4\x10\x03*\xe3\x01\n\x1f\x45SteamDeckCompatibilityCategory\x12-\n)k_ESteamDeckCompatibilityCategory_Unknown\x10\x00\x12\x31\n-k_ESteamDeckCompatibilityCategory_Unsupported\x10\x01\x12.\n*k_ESteamDeckCompatibilityCategory_Playable\x10\x02\x12.\n*k_ESteamDeckCompatibilityCategory_Verified\x10\x03*\xd0\x02\n(ESteamDeckCompatibilityResultDisplayType\x12\x38\n4k_ESteamDeckCompatibilityResultDisplayType_Invisible\x10\x00\x12<\n8k_ESteamDeckCompatibilityResultDisplayType_Informational\x10\x01\x12:\n6k_ESteamDeckCompatibilityResultDisplayType_Unsupported\x10\x02\x12\x37\n3k_ESteamDeckCompatibilityResultDisplayType_Playable\x10\x03\x12\x37\n3k_ESteamDeckCompatibilityResultDisplayType_Verified\x10\x04*w\n\x08\x45\x41\x43State\x12\x16\n\x12k_EACState_Unknown\x10\x00\x12\x1b\n\x17k_EACState_Disconnected\x10\x01\x12\x18\n\x14k_EACState_Connected\x10\x02\x12\x1c\n\x18k_EACState_ConnectedSlow\x10\x03*\x85\x01\n\rEBatteryState\x12\x1b\n\x17k_EBatteryState_Unknown\x10\x00\x12\x1f\n\x1bk_EBatteryState_Discharging\x10\x01\x12\x1c\n\x18k_EBatteryState_Charging\x10\x02\x12\x18\n\x14k_EBatteryState_Full\x10\x03*\xaa\x01\n\tEOSBranch\x12\x17\n\x13k_EOSBranch_Unknown\x10\x00\x12\x17\n\x13k_EOSBranch_Release\x10\x01\x12 \n\x1ck_EOSBranch_ReleaseCandidate\x10\x02\x12\x14\n\x10k_EOSBranch_Beta\x10\x03\x12\x1d\n\x19k_EOSBranch_BetaCandidate\x10\x04\x12\x14\n\x10k_EOSBranch_Main\x10\x05*\xac\x05\n\x13\x45\x43ommunityItemClass\x12!\n\x1dk_ECommunityItemClass_Invalid\x10\x00\x12\x1f\n\x1bk_ECommunityItemClass_Badge\x10\x01\x12\"\n\x1ek_ECommunityItemClass_GameCard\x10\x02\x12+\n\'k_ECommunityItemClass_ProfileBackground\x10\x03\x12\"\n\x1ek_ECommunityItemClass_Emoticon\x10\x04\x12%\n!k_ECommunityItemClass_BoosterPack\x10\x05\x12$\n k_ECommunityItemClass_Consumable\x10\x06\x12!\n\x1dk_ECommunityItemClass_GameGoo\x10\x07\x12)\n%k_ECommunityItemClass_ProfileModifier\x10\x08\x12\x1f\n\x1bk_ECommunityItemClass_Scene\x10\t\x12$\n k_ECommunityItemClass_SalienItem\x10\n\x12!\n\x1dk_ECommunityItemClass_Sticker\x10\x0b\x12$\n k_ECommunityItemClass_ChatEffect\x10\x0c\x12/\n+k_ECommunityItemClass_MiniProfileBackground\x10\r\x12%\n!k_ECommunityItemClass_AvatarFrame\x10\x0e\x12(\n$k_ECommunityItemClass_AnimatedAvatar\x10\x0f\x12/\n+k_ECommunityItemClass_SteamDeckKeyboardSkin\x10\x10*\xd9\x01\n\x1f\x45SteamDeckCompatibilityFeedback\x12+\n\'k_ESteamDeckCompatibilityFeedback_Unset\x10\x00\x12+\n\'k_ESteamDeckCompatibilityFeedback_Agree\x10\x01\x12.\n*k_ESteamDeckCompatibilityFeedback_Disagree\x10\x02\x12,\n(k_ESteamDeckCompatibilityFeedback_Ignore\x10\x03*\x9f\x01\n\x1e\x45ProvideDeckFeedbackPreference\x12*\n&k_EProvideDeckFeedbackPreference_Unset\x10\x00\x12(\n$k_EProvideDeckFeedbackPreference_Yes\x10\x01\x12\'\n#k_EProvideDeckFeedbackPreference_No\x10\x02*\xb1\x03\n\rETouchGesture\x12\x17\n\x13k_ETouchGestureNone\x10\x00\x12\x18\n\x14k_ETouchGestureTouch\x10\x01\x12\x16\n\x12k_ETouchGestureTap\x10\x02\x12\x1c\n\x18k_ETouchGestureDoubleTap\x10\x03\x12\x1d\n\x19k_ETouchGestureShortPress\x10\x04\x12\x1c\n\x18k_ETouchGestureLongPress\x10\x05\x12\x1a\n\x16k_ETouchGestureLongTap\x10\x06\x12\x1f\n\x1bk_ETouchGestureTwoFingerTap\x10\x07\x12\x1f\n\x1bk_ETouchGestureTapCancelled\x10\x08\x12\x1d\n\x19k_ETouchGesturePinchBegin\x10\t\x12\x1e\n\x1ak_ETouchGesturePinchUpdate\x10\n\x12\x1b\n\x17k_ETouchGesturePinchEnd\x10\x0b\x12\x1d\n\x19k_ETouchGestureFlingStart\x10\x0c\x12!\n\x1dk_ETouchGestureFlingCancelled\x10\r*\x8c\x01\n\x13\x45SessionPersistence\x12*\n\x1dk_ESessionPersistence_Invalid\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12#\n\x1fk_ESessionPersistence_Ephemeral\x10\x00\x12$\n k_ESessionPersistence_Persistent\x10\x01\x42\tH\x01\x80\x01\x01\x80\xb5\x18\x01')

_EPUBLISHEDFILEQUERYTYPE = DESCRIPTOR.enum_types_by_name['EPublishedFileQueryType']
EPublishedFileQueryType = enum_type_wrapper.EnumTypeWrapper(
    _EPUBLISHEDFILEQUERYTYPE)
_EPUBLISHEDFILEINAPPROPRIATEPROVIDER = DESCRIPTOR.enum_types_by_name[
    'EPublishedFileInappropriateProvider']
EPublishedFileInappropriateProvider = enum_type_wrapper.EnumTypeWrapper(
    _EPUBLISHEDFILEINAPPROPRIATEPROVIDER)
_EPUBLISHEDFILEINAPPROPRIATERESULT = DESCRIPTOR.enum_types_by_name[
    'EPublishedFileInappropriateResult']
EPublishedFileInappropriateResult = enum_type_wrapper.EnumTypeWrapper(
    _EPUBLISHEDFILEINAPPROPRIATERESULT)
_EPERSONASTATEFLAG = DESCRIPTOR.enum_types_by_name['EPersonaStateFlag']
EPersonaStateFlag = enum_type_wrapper.EnumTypeWrapper(_EPERSONASTATEFLAG)
_ECONTENTCHECKPROVIDER = DESCRIPTOR.enum_types_by_name['EContentCheckProvider']
EContentCheckProvider = enum_type_wrapper.EnumTypeWrapper(
    _ECONTENTCHECKPROVIDER)
_EPROFILECUSTOMIZATIONTYPE = DESCRIPTOR.enum_types_by_name['EProfileCustomizationType']
EProfileCustomizationType = enum_type_wrapper.EnumTypeWrapper(
    _EPROFILECUSTOMIZATIONTYPE)
_EPUBLISHEDFILESTORAGESYSTEM = DESCRIPTOR.enum_types_by_name['EPublishedFileStorageSystem']
EPublishedFileStorageSystem = enum_type_wrapper.EnumTypeWrapper(
    _EPUBLISHEDFILESTORAGESYSTEM)
_ECLOUDSTORAGEPERSISTSTATE = DESCRIPTOR.enum_types_by_name['ECloudStoragePersistState']
ECloudStoragePersistState = enum_type_wrapper.EnumTypeWrapper(
    _ECLOUDSTORAGEPERSISTSTATE)
_ESDCARDFORMATSTAGE = DESCRIPTOR.enum_types_by_name['ESDCardFormatStage']
ESDCardFormatStage = enum_type_wrapper.EnumTypeWrapper(_ESDCARDFORMATSTAGE)
_ESYSTEMFANCONTROLMODE = DESCRIPTOR.enum_types_by_name['ESystemFanControlMode']
ESystemFanControlMode = enum_type_wrapper.EnumTypeWrapper(
    _ESYSTEMFANCONTROLMODE)
_ECOLORPROFILE = DESCRIPTOR.enum_types_by_name['EColorProfile']
EColorProfile = enum_type_wrapper.EnumTypeWrapper(_ECOLORPROFILE)
_EBLUETOOTHDEVICETYPE = DESCRIPTOR.enum_types_by_name['EBluetoothDeviceType']
EBluetoothDeviceType = enum_type_wrapper.EnumTypeWrapper(_EBLUETOOTHDEVICETYPE)
_ESYSTEMAUDIODIRECTION = DESCRIPTOR.enum_types_by_name['ESystemAudioDirection']
ESystemAudioDirection = enum_type_wrapper.EnumTypeWrapper(
    _ESYSTEMAUDIODIRECTION)
_ESYSTEMAUDIOCHANNEL = DESCRIPTOR.enum_types_by_name['ESystemAudioChannel']
ESystemAudioChannel = enum_type_wrapper.EnumTypeWrapper(_ESYSTEMAUDIOCHANNEL)
_ESYSTEMAUDIOPORTTYPE = DESCRIPTOR.enum_types_by_name['ESystemAudioPortType']
ESystemAudioPortType = enum_type_wrapper.EnumTypeWrapper(_ESYSTEMAUDIOPORTTYPE)
_ESYSTEMAUDIOPORTDIRECTION = DESCRIPTOR.enum_types_by_name['ESystemAudioPortDirection']
ESystemAudioPortDirection = enum_type_wrapper.EnumTypeWrapper(
    _ESYSTEMAUDIOPORTDIRECTION)
_ESYSTEMSERVICESTATE = DESCRIPTOR.enum_types_by_name['ESystemServiceState']
ESystemServiceState = enum_type_wrapper.EnumTypeWrapper(_ESYSTEMSERVICESTATE)
_EGRAPHICSPERFOVERLAYLEVEL = DESCRIPTOR.enum_types_by_name['EGraphicsPerfOverlayLevel']
EGraphicsPerfOverlayLevel = enum_type_wrapper.EnumTypeWrapper(
    _EGRAPHICSPERFOVERLAYLEVEL)
_EGPUPERFORMANCELEVEL = DESCRIPTOR.enum_types_by_name['EGPUPerformanceLevel']
EGPUPerformanceLevel = enum_type_wrapper.EnumTypeWrapper(_EGPUPERFORMANCELEVEL)
_ESCALINGFILTER = DESCRIPTOR.enum_types_by_name['EScalingFilter']
EScalingFilter = enum_type_wrapper.EnumTypeWrapper(_ESCALINGFILTER)
_ECPUGOVERNOR = DESCRIPTOR.enum_types_by_name['ECPUGovernor']
ECPUGovernor = enum_type_wrapper.EnumTypeWrapper(_ECPUGOVERNOR)
_EUPDATERTYPE = DESCRIPTOR.enum_types_by_name['EUpdaterType']
EUpdaterType = enum_type_wrapper.EnumTypeWrapper(_EUPDATERTYPE)
_EUPDATERSTATE = DESCRIPTOR.enum_types_by_name['EUpdaterState']
EUpdaterState = enum_type_wrapper.EnumTypeWrapper(_EUPDATERSTATE)
_ESTORAGEBLOCKCONTENTTYPE = DESCRIPTOR.enum_types_by_name['EStorageBlockContentType']
EStorageBlockContentType = enum_type_wrapper.EnumTypeWrapper(
    _ESTORAGEBLOCKCONTENTTYPE)
_ESTORAGEBLOCKFILESYSTEMTYPE = DESCRIPTOR.enum_types_by_name['EStorageBlockFileSystemType']
EStorageBlockFileSystemType = enum_type_wrapper.EnumTypeWrapper(
    _ESTORAGEBLOCKFILESYSTEMTYPE)
_ESTEAMDECKCOMPATIBILITYCATEGORY = DESCRIPTOR.enum_types_by_name[
    'ESteamDeckCompatibilityCategory']
ESteamDeckCompatibilityCategory = enum_type_wrapper.EnumTypeWrapper(
    _ESTEAMDECKCOMPATIBILITYCATEGORY)
_ESTEAMDECKCOMPATIBILITYRESULTDISPLAYTYPE = DESCRIPTOR.enum_types_by_name[
    'ESteamDeckCompatibilityResultDisplayType']
ESteamDeckCompatibilityResultDisplayType = enum_type_wrapper.EnumTypeWrapper(
    _ESTEAMDECKCOMPATIBILITYRESULTDISPLAYTYPE)
_EACSTATE = DESCRIPTOR.enum_types_by_name['EACState']
EACState = enum_type_wrapper.EnumTypeWrapper(_EACSTATE)
_EBATTERYSTATE = DESCRIPTOR.enum_types_by_name['EBatteryState']
EBatteryState = enum_type_wrapper.EnumTypeWrapper(_EBATTERYSTATE)
_EOSBRANCH = DESCRIPTOR.enum_types_by_name['EOSBranch']
EOSBranch = enum_type_wrapper.EnumTypeWrapper(_EOSBRANCH)
_ECOMMUNITYITEMCLASS = DESCRIPTOR.enum_types_by_name['ECommunityItemClass']
ECommunityItemClass = enum_type_wrapper.EnumTypeWrapper(_ECOMMUNITYITEMCLASS)
_ESTEAMDECKCOMPATIBILITYFEEDBACK = DESCRIPTOR.enum_types_by_name[
    'ESteamDeckCompatibilityFeedback']
ESteamDeckCompatibilityFeedback = enum_type_wrapper.EnumTypeWrapper(
    _ESTEAMDECKCOMPATIBILITYFEEDBACK)
_EPROVIDEDECKFEEDBACKPREFERENCE = DESCRIPTOR.enum_types_by_name[
    'EProvideDeckFeedbackPreference']
EProvideDeckFeedbackPreference = enum_type_wrapper.EnumTypeWrapper(
    _EPROVIDEDECKFEEDBACKPREFERENCE)
_ETOUCHGESTURE = DESCRIPTOR.enum_types_by_name['ETouchGesture']
ETouchGesture = enum_type_wrapper.EnumTypeWrapper(_ETOUCHGESTURE)
_ESESSIONPERSISTENCE = DESCRIPTOR.enum_types_by_name['ESessionPersistence']
ESessionPersistence = enum_type_wrapper.EnumTypeWrapper(_ESESSIONPERSISTENCE)
k_PublishedFileQueryType_RankedByVote = 0
k_PublishedFileQueryType_RankedByPublicationDate = 1
k_PublishedFileQueryType_AcceptedForGameRankedByAcceptanceDate = 2
k_PublishedFileQueryType_RankedByTrend = 3
k_PublishedFileQueryType_FavoritedByFriendsRankedByPublicationDate = 4
k_PublishedFileQueryType_CreatedByFriendsRankedByPublicationDate = 5
k_PublishedFileQueryType_RankedByNumTimesReported = 6
k_PublishedFileQueryType_CreatedByFollowedUsersRankedByPublicationDate = 7
k_PublishedFileQueryType_NotYetRated = 8
k_PublishedFileQueryType_RankedByTotalUniqueSubscriptions = 9
k_PublishedFileQueryType_RankedByTotalVotesAsc = 10
k_PublishedFileQueryType_RankedByVotesUp = 11
k_PublishedFileQueryType_RankedByTextSearch = 12
k_PublishedFileQueryType_RankedByPlaytimeTrend = 13
k_PublishedFileQueryType_RankedByTotalPlaytime = 14
k_PublishedFileQueryType_RankedByAveragePlaytimeTrend = 15
k_PublishedFileQueryType_RankedByLifetimeAveragePlaytime = 16
k_PublishedFileQueryType_RankedByPlaytimeSessionsTrend = 17
k_PublishedFileQueryType_RankedByLifetimePlaytimeSessions = 18
k_PublishedFileQueryType_RankedByInappropriateContentRating = 19
k_PublishedFileQueryType_RankedByBanContentCheck = 20
k_PublishedFileQueryType_RankedByLastUpdatedDate = 21
k_EPublishedFileInappropriateProvider_Invalid = 0
k_EPublishedFileInappropriateProvider_Google = 1
k_EPublishedFileInappropriateProvider_Amazon = 2
k_EPublishedFileInappropriateResult_NotScanned = 0
k_EPublishedFileInappropriateResult_VeryUnlikely = 1
k_EPublishedFileInappropriateResult_Unlikely = 30
k_EPublishedFileInappropriateResult_Possible = 50
k_EPublishedFileInappropriateResult_Likely = 75
k_EPublishedFileInappropriateResult_VeryLikely = 100
k_EPersonaStateFlag_HasRichPresence = 1
k_EPersonaStateFlag_InJoinableGame = 2
k_EPersonaStateFlag_Golden = 4
k_EPersonaStateFlag_RemotePlayTogether = 8
k_EPersonaStateFlag_ClientTypeWeb = 256
k_EPersonaStateFlag_ClientTypeMobile = 512
k_EPersonaStateFlag_ClientTypeTenfoot = 1024
k_EPersonaStateFlag_ClientTypeVR = 2048
k_EPersonaStateFlag_LaunchTypeGamepad = 4096
k_EPersonaStateFlag_LaunchTypeCompatTool = 8192
k_EContentCheckProvider_Invalid = 0
k_EContentCheckProvider_Google = 1
k_EContentCheckProvider_Amazon = 2
k_EContentCheckProvider_Local = 3
k_EProfileCustomizationTypeInvalid = 0
k_EProfileCustomizationTypeRareAchievementShowcase = 1
k_EProfileCustomizationTypeGameCollector = 2
k_EProfileCustomizationTypeItemShowcase = 3
k_EProfileCustomizationTypeTradeShowcase = 4
k_EProfileCustomizationTypeBadges = 5
k_EProfileCustomizationTypeFavoriteGame = 6
k_EProfileCustomizationTypeScreenshotShowcase = 7
k_EProfileCustomizationTypeCustomText = 8
k_EProfileCustomizationTypeFavoriteGroup = 9
k_EProfileCustomizationTypeRecommendation = 10
k_EProfileCustomizationTypeWorkshopItem = 11
k_EProfileCustomizationTypeMyWorkshop = 12
k_EProfileCustomizationTypeArtworkShowcase = 13
k_EProfileCustomizationTypeVideoShowcase = 14
k_EProfileCustomizationTypeGuides = 15
k_EProfileCustomizationTypeMyGuides = 16
k_EProfileCustomizationTypeAchievements = 17
k_EProfileCustomizationTypeGreenlight = 18
k_EProfileCustomizationTypeMyGreenlight = 19
k_EProfileCustomizationTypeSalien = 20
k_EProfileCustomizationTypeLoyaltyRewardReactions = 21
k_EProfileCustomizationTypeSingleArtworkShowcase = 22
k_EProfileCustomizationTypeAchievementsCompletionist = 23
k_EPublishedFileStorageSystemInvalid = 0
k_EPublishedFileStorageSystemLegacyCloud = 1
k_EPublishedFileStorageSystemDepot = 2
k_EPublishedFileStorageSystemUGCCloud = 3
k_ECloudStoragePersistStatePersisted = 0
k_ECloudStoragePersistStateForgotten = 1
k_ECloudStoragePersistStateDeleted = 2
k_ESDCardFormatStage_Invalid = 0
k_ESDCardFormatStage_Starting = 1
k_ESDCardFormatStage_Testing = 2
k_ESDCardFormatStage_Rescuing = 3
k_ESDCardFormatStage_Formatting = 4
k_ESDCardFormatStage_Finalizing = 5
k_SystemFanControlMode_Invalid = 0
k_SystemFanControlMode_Disabled = 1
k_SystemFanControlMode_Default = 2
k_EColorProfile_Invalid = 0
k_EColorProfile_Native = 1
k_EColorProfile_Standard = 2
k_EColorProfile_Vivid = 3
k_BluetoothDeviceType_Invalid = 0
k_BluetoothDeviceType_Unknown = 1
k_BluetoothDeviceType_Phone = 2
k_BluetoothDeviceType_Computer = 3
k_BluetoothDeviceType_Headset = 4
k_BluetoothDeviceType_Headphones = 5
k_BluetoothDeviceType_Speakers = 6
k_BluetoothDeviceType_OtherAudio = 7
k_BluetoothDeviceType_Mouse = 8
k_BluetoothDeviceType_Joystick = 9
k_BluetoothDeviceType_Gamepad = 10
k_BluetoothDeviceType_Keyboard = 11
k_SystemAudioDirection_Invalid = 0
k_SystemAudioDirection_Input = 1
k_SystemAudioDirection_Output = 2
k_SystemAudioChannel_Invalid = 0
k_SystemAudioChannel_Aggregated = 1
k_SystemAudioChannel_FrontLeft = 2
k_SystemAudioChannel_FrontRight = 3
k_SystemAudioChannel_LFE = 4
k_SystemAudioChannel_BackLeft = 5
k_SystemAudioChannel_BackRight = 6
k_SystemAudioChannel_FrontCenter = 7
k_SystemAudioChannel_Unknown = 8
k_SystemAudioChannel_Mono = 9
k_SystemAudioPortType_Invalid = 0
k_SystemAudioPortType_Unknown = 1
k_SystemAudioPortType_Audio32f = 2
k_SystemAudioPortType_Midi8b = 3
k_SystemAudioPortType_Video32RGBA = 4
k_SystemAudioPortDirection_Invalid = 0
k_SystemAudioPortDirection_Input = 1
k_SystemAudioPortDirection_Output = 2
k_ESystemServiceState_Unavailable = 0
k_ESystemServiceState_Disabled = 1
k_ESystemServiceState_Enabled = 2
k_EGraphicsPerfOverlayLevel_Hidden = 0
k_EGraphicsPerfOverlayLevel_Basic = 1
k_EGraphicsPerfOverlayLevel_Medium = 2
k_EGraphicsPerfOverlayLevel_Full = 3
k_EGraphicsPerfOverlayLevel_Minimal = 4
k_EGPUPerformanceLevel_Invalid = 0
k_EGPUPerformanceLevel_Auto = 1
k_EGPUPerformanceLevel_Manual = 2
k_EGPUPerformanceLevel_Low = 3
k_EGPUPerformanceLevel_High = 4
k_EGPUPerformanceLevel_Profiling = 5
k_EScalingFilter_Invalid = 0
k_EScalingFilter_FSR = 1
k_EScalingFilter_Nearest = 2
k_EScalingFilter_Integer = 3
k_EScalingFilter_Linear = 4
k_EScalingFilter_NIS = 5
k_ECPUGovernor_Invalid = 0
k_ECPUGovernor_Perf = 1
k_ECPUGovernor_Powersave = 2
k_ECPUGovernor_Manual = 3
k_EUpdaterType_Invalid = 0
k_EUpdaterType_Client = 1
k_EUpdaterType_OS = 2
k_EUpdaterType_BIOS = 3
k_EUpdaterType_Aggregated = 4
k_EUpdaterType_Test1 = 5
k_EUpdaterType_Test2 = 6
k_EUpdaterType_Dummy = 7
k_EUpdaterState_Invalid = 0
k_EUpdaterState_UpToDate = 2
k_EUpdaterState_Checking = 3
k_EUpdaterState_Available = 4
k_EUpdaterState_Applying = 5
k_EUpdaterState_ClientRestartPending = 6
k_EUpdaterState_SystemRestartPending = 7
k_EStorageBlockContentType_Invalid = 0
k_EStorageBlockContentType_Unknown = 1
k_EStorageBlockContentType_FileSystem = 2
k_EStorageBlockContentType_Crypto = 3
k_EStorageBlockContentType_Raid = 4
k_EStorageBlockFileSystemType_Invalid = 0
k_EStorageBlockFileSystemType_Unknown = 1
k_EStorageBlockFileSystemType_VFat = 2
k_EStorageBlockFileSystemType_Ext4 = 3
k_ESteamDeckCompatibilityCategory_Unknown = 0
k_ESteamDeckCompatibilityCategory_Unsupported = 1
k_ESteamDeckCompatibilityCategory_Playable = 2
k_ESteamDeckCompatibilityCategory_Verified = 3
k_ESteamDeckCompatibilityResultDisplayType_Invisible = 0
k_ESteamDeckCompatibilityResultDisplayType_Informational = 1
k_ESteamDeckCompatibilityResultDisplayType_Unsupported = 2
k_ESteamDeckCompatibilityResultDisplayType_Playable = 3
k_ESteamDeckCompatibilityResultDisplayType_Verified = 4
k_EACState_Unknown = 0
k_EACState_Disconnected = 1
k_EACState_Connected = 2
k_EACState_ConnectedSlow = 3
k_EBatteryState_Unknown = 0
k_EBatteryState_Discharging = 1
k_EBatteryState_Charging = 2
k_EBatteryState_Full = 3
k_EOSBranch_Unknown = 0
k_EOSBranch_Release = 1
k_EOSBranch_ReleaseCandidate = 2
k_EOSBranch_Beta = 3
k_EOSBranch_BetaCandidate = 4
k_EOSBranch_Main = 5
k_ECommunityItemClass_Invalid = 0
k_ECommunityItemClass_Badge = 1
k_ECommunityItemClass_GameCard = 2
k_ECommunityItemClass_ProfileBackground = 3
k_ECommunityItemClass_Emoticon = 4
k_ECommunityItemClass_BoosterPack = 5
k_ECommunityItemClass_Consumable = 6
k_ECommunityItemClass_GameGoo = 7
k_ECommunityItemClass_ProfileModifier = 8
k_ECommunityItemClass_Scene = 9
k_ECommunityItemClass_SalienItem = 10
k_ECommunityItemClass_Sticker = 11
k_ECommunityItemClass_ChatEffect = 12
k_ECommunityItemClass_MiniProfileBackground = 13
k_ECommunityItemClass_AvatarFrame = 14
k_ECommunityItemClass_AnimatedAvatar = 15
k_ECommunityItemClass_SteamDeckKeyboardSkin = 16
k_ESteamDeckCompatibilityFeedback_Unset = 0
k_ESteamDeckCompatibilityFeedback_Agree = 1
k_ESteamDeckCompatibilityFeedback_Disagree = 2
k_ESteamDeckCompatibilityFeedback_Ignore = 3
k_EProvideDeckFeedbackPreference_Unset = 0
k_EProvideDeckFeedbackPreference_Yes = 1
k_EProvideDeckFeedbackPreference_No = 2
k_ETouchGestureNone = 0
k_ETouchGestureTouch = 1
k_ETouchGestureTap = 2
k_ETouchGestureDoubleTap = 3
k_ETouchGestureShortPress = 4
k_ETouchGestureLongPress = 5
k_ETouchGestureLongTap = 6
k_ETouchGestureTwoFingerTap = 7
k_ETouchGestureTapCancelled = 8
k_ETouchGesturePinchBegin = 9
k_ETouchGesturePinchUpdate = 10
k_ETouchGesturePinchEnd = 11
k_ETouchGestureFlingStart = 12
k_ETouchGestureFlingCancelled = 13
k_ESessionPersistence_Invalid = -1
k_ESessionPersistence_Ephemeral = 0
k_ESessionPersistence_Persistent = 1


if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'H\001\200\001\001\200\265\030\001'
    _EPUBLISHEDFILEQUERYTYPE._serialized_start = 42
    _EPUBLISHEDFILEQUERYTYPE._serialized_end = 1322
    _EPUBLISHEDFILEINAPPROPRIATEPROVIDER._serialized_start = 1325
    _EPUBLISHEDFILEINAPPROPRIATEPROVIDER._serialized_end = 1513
    _EPUBLISHEDFILEINAPPROPRIATERESULT._serialized_start = 1516
    _EPUBLISHEDFILEINAPPROPRIATERESULT._serialized_end = 1857
    _EPERSONASTATEFLAG._serialized_start = 1860
    _EPERSONASTATEFLAG._serialized_end = 2293
    _ECONTENTCHECKPROVIDER._serialized_start = 2296
    _ECONTENTCHECKPROVIDER._serialized_end = 2463
    _EPROFILECUSTOMIZATIONTYPE._serialized_start = 2466
    _EPROFILECUSTOMIZATIONTYPE._serialized_end = 3598
    _EPUBLISHEDFILESTORAGESYSTEM._serialized_start = 3601
    _EPUBLISHEDFILESTORAGESYSTEM._serialized_end = 3801
    _ECLOUDSTORAGEPERSISTSTATE._serialized_start = 3804
    _ECLOUDSTORAGEPERSISTSTATE._serialized_end = 3955
    _ESDCARDFORMATSTAGE._serialized_start = 3958
    _ESDCARDFORMATSTAGE._serialized_end = 4190
    _ESYSTEMFANCONTROLMODE._serialized_start = 4193
    _ESYSTEMFANCONTROLMODE._serialized_end = 4325
    _ECOLORPROFILE._serialized_start = 4328
    _ECOLORPROFILE._serialized_end = 4457
    _EBLUETOOTHDEVICETYPE._serialized_start = 4460
    _EBLUETOOTHDEVICETYPE._serialized_end = 4908
    _ESYSTEMAUDIODIRECTION._serialized_start = 4911
    _ESYSTEMAUDIODIRECTION._serialized_end = 5039
    _ESYSTEMAUDIOCHANNEL._serialized_start = 5042
    _ESYSTEMAUDIOCHANNEL._serialized_end = 5411
    _ESYSTEMAUDIOPORTTYPE._serialized_start = 5414
    _ESYSTEMAUDIOPORTTYPE._serialized_end = 5615
    _ESYSTEMAUDIOPORTDIRECTION._serialized_start = 5618
    _ESYSTEMAUDIOPORTDIRECTION._serialized_end = 5762
    _ESYSTEMSERVICESTATE._serialized_start = 5765
    _ESYSTEMSERVICESTATE._serialized_end = 5896
    _EGRAPHICSPERFOVERLAYLEVEL._serialized_start = 5899
    _EGRAPHICSPERFOVERLAYLEVEL._serialized_end = 6124
    _EGPUPERFORMANCELEVEL._serialized_start = 6127
    _EGPUPERFORMANCELEVEL._serialized_end = 6356
    _ESCALINGFILTER._serialized_start = 6359
    _ESCALINGFILTER._serialized_end = 6546
    _ECPUGOVERNOR._serialized_start = 6548
    _ECPUGOVERNOR._serialized_end = 6672
    _EUPDATERTYPE._serialized_start = 6675
    _EUPDATERTYPE._serialized_end = 6901
    _EUPDATERSTATE._serialized_start = 6904
    _EUPDATERSTATE._serialized_end = 7153
    _ESTORAGEBLOCKCONTENTTYPE._serialized_start = 7156
    _ESTORAGEBLOCKCONTENTTYPE._serialized_end = 7381
    _ESTORAGEBLOCKFILESYSTEMTYPE._serialized_start = 7384
    _ESTORAGEBLOCKFILESYSTEMTYPE._serialized_end = 7579
    _ESTEAMDECKCOMPATIBILITYCATEGORY._serialized_start = 7582
    _ESTEAMDECKCOMPATIBILITYCATEGORY._serialized_end = 7809
    _ESTEAMDECKCOMPATIBILITYRESULTDISPLAYTYPE._serialized_start = 7812
    _ESTEAMDECKCOMPATIBILITYRESULTDISPLAYTYPE._serialized_end = 8148
    _EACSTATE._serialized_start = 8150
    _EACSTATE._serialized_end = 8269
    _EBATTERYSTATE._serialized_start = 8272
    _EBATTERYSTATE._serialized_end = 8405
    _EOSBRANCH._serialized_start = 8408
    _EOSBRANCH._serialized_end = 8578
    _ECOMMUNITYITEMCLASS._serialized_start = 8581
    _ECOMMUNITYITEMCLASS._serialized_end = 9265
    _ESTEAMDECKCOMPATIBILITYFEEDBACK._serialized_start = 9268
    _ESTEAMDECKCOMPATIBILITYFEEDBACK._serialized_end = 9485
    _EPROVIDEDECKFEEDBACKPREFERENCE._serialized_start = 9488
    _EPROVIDEDECKFEEDBACKPREFERENCE._serialized_end = 9647
    _ETOUCHGESTURE._serialized_start = 9650
    _ETOUCHGESTURE._serialized_end = 10083
    _ESESSIONPERSISTENCE._serialized_start = 10086
    _ESESSIONPERSISTENCE._serialized_end = 10226
# @@protoc_insertion_point(module_scope)
