from __future__ import absolute_import
import os

from .client import Client
from ...exceptions import PureError
from ...properties import Property, Filter
from ...responses import ValidResponse, ErrorResponse, ApiError, ResponseHeaders

from .models.active_directory_patch import ActiveDirectoryPatch
from .models.active_directory_post import ActiveDirectoryPost
from .models.admin_post import AdminPost
from .models.admin_settings import AdminSettings
from .models.admin_settings_required_authentication_methods import AdminSettingsRequiredAuthenticationMethods
from .models.aggregate_replication_performance import AggregateReplicationPerformance
from .models.alert_rules import AlertRules
from .models.alert_rules_catalog import AlertRulesCatalog
from .models.alert_watcher_patch import AlertWatcherPatch
from .models.alert_watcher_post import AlertWatcherPost
from .models.api_client import ApiClient
from .models.api_client_patch import ApiClientPatch
from .models.api_client_post import ApiClientPost
from .models.api_token import ApiToken
from .models.app_node import AppNode
from .models.array_connection_key import ArrayConnectionKey
from .models.array_connection_post import ArrayConnectionPost
from .models.array_encryption import ArrayEncryption
from .models.array_erasure_patch import ArrayErasurePatch
from .models.arrayencryption_data_at_rest import ArrayencryptionDataAtRest
from .models.built_in import BuiltIn
from .models.built_in_relationship import BuiltInRelationship
from .models.built_in_resource_no_id import BuiltInResourceNoId
from .models.certificate_signing_request import CertificateSigningRequest
from .models.certificate_signing_request_post import CertificateSigningRequestPost
from .models.chap import Chap
from .models.cloud_capacity_step import CloudCapacityStep
from .models.cloud_provider_tag import CloudProviderTag
from .models.connection import Connection
from .models.connection_post import ConnectionPost
from .models.container_default_protection import ContainerDefaultProtection
from .models.destroyed_patch_post import DestroyedPatchPost
from .models.directory_export_patch import DirectoryExportPatch
from .models.directory_export_post import DirectoryExportPost
from .models.directory_lock_nlm_reclamation import DirectoryLockNlmReclamation
from .models.directory_policy_export_post import DirectoryPolicyExportPost
from .models.directory_policy_post import DirectoryPolicyPost
from .models.directory_post import DirectoryPost
from .models.directory_quota import DirectoryQuota
from .models.directory_service_management import DirectoryServiceManagement
from .models.directory_snapshot_post import DirectorySnapshotPost
from .models.directorypolicyexportpost_policies import DirectorypolicyexportpostPolicies
from .models.directorypolicypost_policies import DirectorypolicypostPolicies
from .models.dns_post import DnsPost
from .models.eradication_config import EradicationConfig
from .models.eula import Eula
from .models.eula_signature import EulaSignature
from .models.export_policy_attachment_mixin import ExportPolicyAttachmentMixin
from .models.file_post import FilePost
from .models.fixed_name_resource_no_id import FixedNameResourceNoId
from .models.fixed_reference import FixedReference
from .models.fixed_reference_no_id import FixedReferenceNoId
from .models.host_port_connectivity import HostPortConnectivity
from .models.host_post import HostPost
from .models.kmip import Kmip
from .models.kmip_certificate import KmipCertificate
from .models.kmip_object import KmipObject
from .models.kmip_patch import KmipPatch
from .models.kmip_post import KmipPost
from .models.kmip_test_result import KmipTestResult
from .models.limited_by import LimitedBy
from .models.local_group import LocalGroup
from .models.local_group_membership_post import LocalGroupMembershipPost
from .models.local_group_post import LocalGroupPost
from .models.local_member import LocalMember
from .models.local_user import LocalUser
from .models.local_user_membership_post import LocalUserMembershipPost
from .models.local_user_patch import LocalUserPatch
from .models.local_user_post import LocalUserPost
from .models.localgroupmembershippost_members import LocalgroupmembershippostMembers
from .models.localusermembershippost_groups import LocalusermembershippostGroups
from .models.maintenance_window_post import MaintenanceWindowPost
from .models.mapping_policy_patch import MappingPolicyPatch
from .models.member import Member
from .models.member_no_id_all import MemberNoIdAll
from .models.member_no_id_group import MemberNoIdGroup
from .models.member_no_id_member import MemberNoIdMember
from .models.network_interface_eth import NetworkInterfaceEth
from .models.network_interface_fc import NetworkInterfaceFc
from .models.network_interface_neighbor import NetworkInterfaceNeighbor
from .models.network_interface_neighbor_capability import NetworkInterfaceNeighborCapability
from .models.network_interface_neighbor_neighbor_chassis import NetworkInterfaceNeighborNeighborChassis
from .models.network_interface_neighbor_neighbor_chassis_id import NetworkInterfaceNeighborNeighborChassisId
from .models.network_interface_neighbor_neighbor_port import NetworkInterfaceNeighborNeighborPort
from .models.network_interface_neighbor_neighbor_port_id import NetworkInterfaceNeighborNeighborPortId
from .models.network_interface_patch import NetworkInterfacePatch
from .models.network_interface_performance_eth import NetworkInterfacePerformanceEth
from .models.network_interface_performance_fc import NetworkInterfacePerformanceFc
from .models.network_interface_port_details_rx_los import NetworkInterfacePortDetailsRxLos
from .models.network_interface_port_details_rx_power import NetworkInterfacePortDetailsRxPower
from .models.network_interface_port_details_static import NetworkInterfacePortDetailsStatic
from .models.network_interface_port_details_static_rx_power_thresholds import NetworkInterfacePortDetailsStaticRxPowerThresholds
from .models.network_interface_port_details_static_temperature_thresholds import NetworkInterfacePortDetailsStaticTemperatureThresholds
from .models.network_interface_port_details_static_tx_bias_thresholds import NetworkInterfacePortDetailsStaticTxBiasThresholds
from .models.network_interface_port_details_static_tx_power_thresholds import NetworkInterfacePortDetailsStaticTxPowerThresholds
from .models.network_interface_port_details_static_voltage_thresholds import NetworkInterfacePortDetailsStaticVoltageThresholds
from .models.network_interface_port_details_temperature import NetworkInterfacePortDetailsTemperature
from .models.network_interface_port_details_tx_bias import NetworkInterfacePortDetailsTxBias
from .models.network_interface_port_details_tx_fault import NetworkInterfacePortDetailsTxFault
from .models.network_interface_port_details_tx_power import NetworkInterfacePortDetailsTxPower
from .models.network_interface_port_details_voltage import NetworkInterfacePortDetailsVoltage
from .models.networkinterfacepatch_eth import NetworkinterfacepatchEth
from .models.networkinterfacepost_eth import NetworkinterfacepostEth
from .models.new_name import NewName
from .models.non_copyable_tag import NonCopyableTag
from .models.offload_azure import OffloadAzure
from .models.offload_google_cloud import OffloadGoogleCloud
from .models.offload_nfs import OffloadNfs
from .models.offload_post import OffloadPost
from .models.offload_s3 import OffloadS3
from .models.override_check import OverrideCheck
from .models.page_info import PageInfo
from .models.performance import Performance
from .models.pod_eradication_config import PodEradicationConfig
from .models.pod_performance_replication import PodPerformanceReplication
from .models.pod_replica_link_patch import PodReplicaLinkPatch
from .models.policy_member import PolicyMember
from .models.policy_member_export_post import PolicyMemberExportPost
from .models.policy_member_post import PolicyMemberPost
from .models.policy_nfs_policy_mapping import PolicyNfsPolicyMapping
from .models.policy_post import PolicyPost
from .models.policy_rule_alert_watcher import PolicyRuleAlertWatcher
from .models.policy_rule_alert_watcher_patch import PolicyRuleAlertWatcherPatch
from .models.policy_rule_alert_watcher_post import PolicyRuleAlertWatcherPost
from .models.policy_rule_nfs_client import PolicyRuleNfsClient
from .models.policy_rule_nfs_client_post import PolicyRuleNfsClientPost
from .models.policy_rule_quota import PolicyRuleQuota
from .models.policy_rule_quota_patch import PolicyRuleQuotaPatch
from .models.policy_rule_quota_post import PolicyRuleQuotaPost
from .models.policy_rule_smb_client import PolicyRuleSmbClient
from .models.policy_rule_smb_client_post import PolicyRuleSmbClientPost
from .models.policy_rule_snapshot import PolicyRuleSnapshot
from .models.policy_rule_snapshot_post import PolicyRuleSnapshotPost
from .models.policymemberexportpost_members import PolicymemberexportpostMembers
from .models.policymemberpost_members import PolicymemberpostMembers
from .models.policynfspost_policy_mapping import PolicynfspostPolicyMapping
from .models.policyrulealertwatcherpatch_rules import PolicyrulealertwatcherpatchRules
from .models.policyrulealertwatcherpost_rules import PolicyrulealertwatcherpostRules
from .models.policyrulenfsclientpost_rules import PolicyrulenfsclientpostRules
from .models.policyrulequotapatch_rules import PolicyrulequotapatchRules
from .models.policyrulequotapost_rules import PolicyrulequotapostRules
from .models.policyrulesmbclientpost_rules import PolicyrulesmbclientpostRules
from .models.policyrulesnapshotpost_rules import PolicyrulesnapshotpostRules
from .models.port_common import PortCommon
from .models.port_initiator import PortInitiator
from .models.priority_adjustment import PriorityAdjustment
from .models.protection_group_eradication_config import ProtectionGroupEradicationConfig
from .models.protection_group_target import ProtectionGroupTarget
from .models.protection_groups_volumes import ProtectionGroupsVolumes
from .models.protocol_endpoint import ProtocolEndpoint
from .models.qos import Qos
from .models.reference import Reference
from .models.reference_no_id import ReferenceNoId
from .models.remote_volume_snapshot_post import RemoteVolumeSnapshotPost
from .models.replica_link_lag import ReplicaLinkLag
from .models.replica_link_performance_replication import ReplicaLinkPerformanceReplication
from .models.replication_performance_with_total import ReplicationPerformanceWithTotal
from .models.resource import Resource
from .models.resource_fixed_non_unique_name import ResourceFixedNonUniqueName
from .models.resource_no_id import ResourceNoId
from .models.retention_policy import RetentionPolicy
from .models.saml2_sso_idp import Saml2SsoIdp
from .models.saml2_sso_post import Saml2SsoPost
from .models.saml2_sso_sp_credential import Saml2SsoSpCredential
from .models.smis import Smis
from .models.snapshot import Snapshot
from .models.snapshot_schedule import SnapshotSchedule
from .models.snmp_agent_mib import SnmpAgentMib
from .models.snmp_manager_post import SnmpManagerPost
from .models.snmp_v2c import SnmpV2c
from .models.snmp_v3 import SnmpV3
from .models.snmp_v3_patch import SnmpV3Patch
from .models.snmp_v3_post import SnmpV3Post
from .models.software_bundle_post import SoftwareBundlePost
from .models.software_checks_checks import SoftwareChecksChecks
from .models.software_installation_patch import SoftwareInstallationPatch
from .models.software_installation_post import SoftwareInstallationPost
from .models.software_installation_steps_checks import SoftwareInstallationStepsChecks
from .models.software_post import SoftwarePost
from .models.software_upgrade_plan import SoftwareUpgradePlan
from .models.software_version import SoftwareVersion
from .models.space import Space
from .models.start_end_time import StartEndTime
from .models.subnet_post import SubnetPost
from .models.subscription import Subscription
from .models.subscription_asset_subscription import SubscriptionAssetSubscription
from .models.support_patch import SupportPatch
from .models.support_remote_assist_paths import SupportRemoteAssistPaths
from .models.syslog_server_settings import SyslogServerSettings
from .models.tag import Tag
from .models.target_protection_group import TargetProtectionGroup
from .models.target_protection_group_post_patch import TargetProtectionGroupPostPatch
from .models.test_result import TestResult
from .models.throttle import Throttle
from .models.throttle_deprecated import ThrottleDeprecated
from .models.time_window import TimeWindow
from .models.transfer import Transfer
from .models.username import Username
from .models.vchost_certificate import VchostCertificate
from .models.vchost_certificate_patch import VchostCertificatePatch
from .models.vchost_certificate_post import VchostCertificatePost
from .models.vchost_connection import VchostConnection
from .models.vchost_endpoint import VchostEndpoint
from .models.vchost_endpoint_patch import VchostEndpointPatch
from .models.vchost_endpoint_post import VchostEndpointPost
from .models.vchost_patch import VchostPatch
from .models.vchost_post import VchostPost
from .models.virtual_machine import VirtualMachine
from .models.virtual_machine_post import VirtualMachinePost
from .models.virtual_machine_volume_snapshot import VirtualMachineVolumeSnapshot
from .models.volume_diff import VolumeDiff
from .models.active_directory import ActiveDirectory
from .models.admin import Admin
from .models.admin_api_token import AdminApiToken
from .models.admin_cache import AdminCache
from .models.admin_role import AdminRole
from .models.alert import Alert
from .models.alert_event import AlertEvent
from .models.alert_watcher import AlertWatcher
from .models.app import App
from .models.array_connection import ArrayConnection
from .models.array_connection_patch import ArrayConnectionPatch
from .models.array_connection_path import ArrayConnectionPath
from .models.array_erasure import ArrayErasure
from .models.array_factory_reset_token import ArrayFactoryResetToken
from .models.array_performance import ArrayPerformance
from .models.array_space import ArraySpace
from .models.arrays import Arrays
from .models.audit import Audit
from .models.certificate import Certificate
from .models.cloud_capacity_status import CloudCapacityStatus
from .models.controller import Controller
from .models.default_protection_reference import DefaultProtectionReference
from .models.directory import Directory
from .models.directory_export import DirectoryExport
from .models.directory_patch import DirectoryPatch
from .models.directory_performance import DirectoryPerformance
from .models.directory_service import DirectoryService
from .models.directory_service_role import DirectoryServiceRole
from .models.directory_snapshot import DirectorySnapshot
from .models.directory_snapshot_patch import DirectorySnapshotPatch
from .models.dns import Dns
from .models.dns_patch import DnsPatch
from .models.drive import Drive
from .models.file_system import FileSystem
from .models.file_system_patch import FileSystemPatch
from .models.fixed_reference_with_type import FixedReferenceWithType
from .models.hardware import Hardware
from .models.hardware_patch import HardwarePatch
from .models.host import Host
from .models.host_group import HostGroup
from .models.host_group_patch import HostGroupPatch
from .models.host_patch import HostPatch
from .models.host_performance_balance import HostPerformanceBalance
from .models.log_target import LogTarget
from .models.maintenance_window import MaintenanceWindow
from .models.mapping_policy import MappingPolicy
from .models.network_interface import NetworkInterface
from .models.network_interface_performance import NetworkInterfacePerformance
from .models.network_interface_post import NetworkInterfacePost
from .models.network_interfaces_port_details import NetworkInterfacesPortDetails
from .models.offload import Offload
from .models.pod import Pod
from .models.pod_array_status import PodArrayStatus
from .models.pod_patch import PodPatch
from .models.pod_performance import PodPerformance
from .models.pod_performance_replication import PodPerformanceReplication
from .models.pod_performance_replication_by_array import PodPerformanceReplicationByArray
from .models.pod_post import PodPost
from .models.pod_replica_link import PodReplicaLink
from .models.pod_replica_link_lag import PodReplicaLinkLag
from .models.pod_replica_link_performance_replication import PodReplicaLinkPerformanceReplication
from .models.pod_replica_link_reference import PodReplicaLinkReference
from .models.pod_space import PodSpace
from .models.policy import Policy
from .models.policy_audit_file_post import PolicyAuditFilePost
from .models.policy_member_export import PolicyMemberExport
from .models.policy_nfs_post import PolicyNfsPost
from .models.policy_password import PolicyPassword
from .models.policy_patch import PolicyPatch
from .models.policy_smb_post import PolicySmbPost
from .models.port import Port
from .models.protection_group import ProtectionGroup
from .models.protection_group_performance import ProtectionGroupPerformance
from .models.protection_group_performance_array import ProtectionGroupPerformanceArray
from .models.protection_group_snapshot import ProtectionGroupSnapshot
from .models.protection_group_snapshot_post import ProtectionGroupSnapshotPost
from .models.protection_group_snapshot_replica import ProtectionGroupSnapshotReplica
from .models.protection_group_snapshot_transfer import ProtectionGroupSnapshotTransfer
from .models.protection_groups_volumes_member import ProtectionGroupsVolumesMember
from .models.reference_no_id_with_type import ReferenceNoIdWithType
from .models.reference_with_type import ReferenceWithType
from .models.remote_pod import RemotePod
from .models.remote_protection_group import RemoteProtectionGroup
from .models.remote_protection_group_snapshot import RemoteProtectionGroupSnapshot
from .models.remote_protection_group_snapshot_transfer import RemoteProtectionGroupSnapshotTransfer
from .models.remote_volume_snapshot import RemoteVolumeSnapshot
from .models.remote_volume_snapshot_transfer import RemoteVolumeSnapshotTransfer
from .models.replication_schedule import ReplicationSchedule
from .models.resource_directory_space import ResourceDirectorySpace
from .models.resource_performance import ResourcePerformance
from .models.resource_performance_no_id import ResourcePerformanceNoId
from .models.resource_pod_space import ResourcePodSpace
from .models.resource_space import ResourceSpace
from .models.resource_space_no_id import ResourceSpaceNoId
from .models.saml2_sso import Saml2Sso
from .models.saml2_sso_patch import Saml2SsoPatch
from .models.saml2_sso_sp import Saml2SsoSp
from .models.session import Session
from .models.smtp_server import SmtpServer
from .models.snapshot_space import SnapshotSpace
from .models.snmp_agent import SnmpAgent
from .models.snmp_agent_patch import SnmpAgentPatch
from .models.snmp_manager import SnmpManager
from .models.snmp_manager_patch import SnmpManagerPatch
from .models.software import Software
from .models.software_bundle import SoftwareBundle
from .models.software_check import SoftwareCheck
from .models.software_installation import SoftwareInstallation
from .models.software_installation_step import SoftwareInstallationStep
from .models.software_patch import SoftwarePatch
from .models.space import Space
from .models.subnet import Subnet
from .models.subnet_patch import SubnetPatch
from .models.subscription_asset import SubscriptionAsset
from .models.support import Support
from .models.test_result_with_resource import TestResultWithResource
from .models.test_result_with_resource_with_id import TestResultWithResourceWithId
from .models.vchost import Vchost
from .models.volume_common import VolumeCommon
from .models.volume_group import VolumeGroup
from .models.volume_group_patch import VolumeGroupPatch
from .models.volume_group_performance import VolumeGroupPerformance
from .models.volume_group_post import VolumeGroupPost
from .models.volume_patch import VolumePatch
from .models.volume_performance import VolumePerformance
from .models.volume_post import VolumePost
from .models.volume_snapshot import VolumeSnapshot
from .models.volume_snapshot_patch import VolumeSnapshotPatch
from .models.volume_snapshot_post import VolumeSnapshotPost
from .models.volume_snapshot_transfer import VolumeSnapshotTransfer
from .models.volume_space import VolumeSpace
from .models.volume_space_common import VolumeSpaceCommon
from .models.admin_patch import AdminPatch
from .models.array_performance_by_link import ArrayPerformanceByLink
from .models.certificate_post import CertificatePost
from .models.log_target_file import LogTargetFile
from .models.pod_performance_by_array import PodPerformanceByArray
from .models.policy_audit_file import PolicyAuditFile
from .models.policy_audit_file_patch import PolicyAuditFilePatch
from .models.policy_nfs import PolicyNfs
from .models.policy_nfs_patch import PolicyNfsPatch
from .models.policy_smb import PolicySmb
from .models.policy_smb_patch import PolicySmbPatch
from .models.protection_group_snapshot_patch import ProtectionGroupSnapshotPatch
from .models.remote_protection_group_snapshot_post import RemoteProtectionGroupSnapshotPost
from .models.resource_performance_by_array import ResourcePerformanceByArray
from .models.resource_performance_no_id_by_array import ResourcePerformanceNoIdByArray
from .models.syslog_server import SyslogServer
from .models.volume import Volume
from .models.volume_batch_post import VolumeBatchPost


def add_properties(model):
    for name, value in model.attribute_map.items():
        setattr(model, name, Property(value))


CLASSES_TO_ADD_PROPS = [
    ActiveDirectoryPatch,
    ActiveDirectoryPost,
    AdminPost,
    AdminSettings,
    AdminSettingsRequiredAuthenticationMethods,
    AggregateReplicationPerformance,
    AlertRules,
    AlertRulesCatalog,
    AlertWatcherPatch,
    AlertWatcherPost,
    ApiClient,
    ApiClientPatch,
    ApiClientPost,
    ApiToken,
    AppNode,
    ArrayConnectionKey,
    ArrayConnectionPost,
    ArrayEncryption,
    ArrayErasurePatch,
    ArrayencryptionDataAtRest,
    BuiltIn,
    BuiltInRelationship,
    BuiltInResourceNoId,
    CertificateSigningRequest,
    CertificateSigningRequestPost,
    Chap,
    CloudCapacityStep,
    CloudProviderTag,
    Connection,
    ConnectionPost,
    ContainerDefaultProtection,
    DestroyedPatchPost,
    DirectoryExportPatch,
    DirectoryExportPost,
    DirectoryLockNlmReclamation,
    DirectoryPolicyExportPost,
    DirectoryPolicyPost,
    DirectoryPost,
    DirectoryQuota,
    DirectoryServiceManagement,
    DirectorySnapshotPost,
    DirectorypolicyexportpostPolicies,
    DirectorypolicypostPolicies,
    DnsPost,
    EradicationConfig,
    Eula,
    EulaSignature,
    ExportPolicyAttachmentMixin,
    FilePost,
    FixedNameResourceNoId,
    FixedReference,
    FixedReferenceNoId,
    HostPortConnectivity,
    HostPost,
    Kmip,
    KmipCertificate,
    KmipObject,
    KmipPatch,
    KmipPost,
    KmipTestResult,
    LimitedBy,
    LocalGroup,
    LocalGroupMembershipPost,
    LocalGroupPost,
    LocalMember,
    LocalUser,
    LocalUserMembershipPost,
    LocalUserPatch,
    LocalUserPost,
    LocalgroupmembershippostMembers,
    LocalusermembershippostGroups,
    MaintenanceWindowPost,
    MappingPolicyPatch,
    Member,
    MemberNoIdAll,
    MemberNoIdGroup,
    MemberNoIdMember,
    NetworkInterfaceEth,
    NetworkInterfaceFc,
    NetworkInterfaceNeighbor,
    NetworkInterfaceNeighborCapability,
    NetworkInterfaceNeighborNeighborChassis,
    NetworkInterfaceNeighborNeighborChassisId,
    NetworkInterfaceNeighborNeighborPort,
    NetworkInterfaceNeighborNeighborPortId,
    NetworkInterfacePatch,
    NetworkInterfacePerformanceEth,
    NetworkInterfacePerformanceFc,
    NetworkInterfacePortDetailsRxLos,
    NetworkInterfacePortDetailsRxPower,
    NetworkInterfacePortDetailsStatic,
    NetworkInterfacePortDetailsStaticRxPowerThresholds,
    NetworkInterfacePortDetailsStaticTemperatureThresholds,
    NetworkInterfacePortDetailsStaticTxBiasThresholds,
    NetworkInterfacePortDetailsStaticTxPowerThresholds,
    NetworkInterfacePortDetailsStaticVoltageThresholds,
    NetworkInterfacePortDetailsTemperature,
    NetworkInterfacePortDetailsTxBias,
    NetworkInterfacePortDetailsTxFault,
    NetworkInterfacePortDetailsTxPower,
    NetworkInterfacePortDetailsVoltage,
    NetworkinterfacepatchEth,
    NetworkinterfacepostEth,
    NewName,
    NonCopyableTag,
    OffloadAzure,
    OffloadGoogleCloud,
    OffloadNfs,
    OffloadPost,
    OffloadS3,
    OverrideCheck,
    PageInfo,
    Performance,
    PodEradicationConfig,
    PodPerformanceReplication,
    PodReplicaLinkPatch,
    PolicyMember,
    PolicyMemberExportPost,
    PolicyMemberPost,
    PolicyNfsPolicyMapping,
    PolicyPost,
    PolicyRuleAlertWatcher,
    PolicyRuleAlertWatcherPatch,
    PolicyRuleAlertWatcherPost,
    PolicyRuleNfsClient,
    PolicyRuleNfsClientPost,
    PolicyRuleQuota,
    PolicyRuleQuotaPatch,
    PolicyRuleQuotaPost,
    PolicyRuleSmbClient,
    PolicyRuleSmbClientPost,
    PolicyRuleSnapshot,
    PolicyRuleSnapshotPost,
    PolicymemberexportpostMembers,
    PolicymemberpostMembers,
    PolicynfspostPolicyMapping,
    PolicyrulealertwatcherpatchRules,
    PolicyrulealertwatcherpostRules,
    PolicyrulenfsclientpostRules,
    PolicyrulequotapatchRules,
    PolicyrulequotapostRules,
    PolicyrulesmbclientpostRules,
    PolicyrulesnapshotpostRules,
    PortCommon,
    PortInitiator,
    PriorityAdjustment,
    ProtectionGroupEradicationConfig,
    ProtectionGroupTarget,
    ProtectionGroupsVolumes,
    ProtocolEndpoint,
    Qos,
    Reference,
    ReferenceNoId,
    RemoteVolumeSnapshotPost,
    ReplicaLinkLag,
    ReplicaLinkPerformanceReplication,
    ReplicationPerformanceWithTotal,
    Resource,
    ResourceFixedNonUniqueName,
    ResourceNoId,
    RetentionPolicy,
    Saml2SsoIdp,
    Saml2SsoPost,
    Saml2SsoSpCredential,
    Smis,
    Snapshot,
    SnapshotSchedule,
    SnmpAgentMib,
    SnmpManagerPost,
    SnmpV2c,
    SnmpV3,
    SnmpV3Patch,
    SnmpV3Post,
    SoftwareBundlePost,
    SoftwareChecksChecks,
    SoftwareInstallationPatch,
    SoftwareInstallationPost,
    SoftwareInstallationStepsChecks,
    SoftwarePost,
    SoftwareUpgradePlan,
    SoftwareVersion,
    Space,
    StartEndTime,
    SubnetPost,
    Subscription,
    SubscriptionAssetSubscription,
    SupportPatch,
    SupportRemoteAssistPaths,
    SyslogServerSettings,
    Tag,
    TargetProtectionGroup,
    TargetProtectionGroupPostPatch,
    TestResult,
    Throttle,
    ThrottleDeprecated,
    TimeWindow,
    Transfer,
    Username,
    VchostCertificate,
    VchostCertificatePatch,
    VchostCertificatePost,
    VchostConnection,
    VchostEndpoint,
    VchostEndpointPatch,
    VchostEndpointPost,
    VchostPatch,
    VchostPost,
    VirtualMachine,
    VirtualMachinePost,
    VirtualMachineVolumeSnapshot,
    VolumeDiff,
    ActiveDirectory,
    Admin,
    AdminApiToken,
    AdminCache,
    AdminRole,
    Alert,
    AlertEvent,
    AlertWatcher,
    App,
    ArrayConnection,
    ArrayConnectionPatch,
    ArrayConnectionPath,
    ArrayErasure,
    ArrayFactoryResetToken,
    ArrayPerformance,
    ArraySpace,
    Arrays,
    Audit,
    Certificate,
    CloudCapacityStatus,
    Controller,
    DefaultProtectionReference,
    Directory,
    DirectoryExport,
    DirectoryPatch,
    DirectoryPerformance,
    DirectoryService,
    DirectoryServiceRole,
    DirectorySnapshot,
    DirectorySnapshotPatch,
    Dns,
    DnsPatch,
    Drive,
    FileSystem,
    FileSystemPatch,
    FixedReferenceWithType,
    Hardware,
    HardwarePatch,
    Host,
    HostGroup,
    HostGroupPatch,
    HostPatch,
    HostPerformanceBalance,
    LogTarget,
    MaintenanceWindow,
    MappingPolicy,
    NetworkInterface,
    NetworkInterfacePerformance,
    NetworkInterfacePost,
    NetworkInterfacesPortDetails,
    Offload,
    Pod,
    PodArrayStatus,
    PodPatch,
    PodPerformance,
    PodPerformanceReplication,
    PodPerformanceReplicationByArray,
    PodPost,
    PodReplicaLink,
    PodReplicaLinkLag,
    PodReplicaLinkPerformanceReplication,
    PodReplicaLinkReference,
    PodSpace,
    Policy,
    PolicyAuditFilePost,
    PolicyMemberExport,
    PolicyNfsPost,
    PolicyPassword,
    PolicyPatch,
    PolicySmbPost,
    Port,
    ProtectionGroup,
    ProtectionGroupPerformance,
    ProtectionGroupPerformanceArray,
    ProtectionGroupSnapshot,
    ProtectionGroupSnapshotPost,
    ProtectionGroupSnapshotReplica,
    ProtectionGroupSnapshotTransfer,
    ProtectionGroupsVolumesMember,
    ReferenceNoIdWithType,
    ReferenceWithType,
    RemotePod,
    RemoteProtectionGroup,
    RemoteProtectionGroupSnapshot,
    RemoteProtectionGroupSnapshotTransfer,
    RemoteVolumeSnapshot,
    RemoteVolumeSnapshotTransfer,
    ReplicationSchedule,
    ResourceDirectorySpace,
    ResourcePerformance,
    ResourcePerformanceNoId,
    ResourcePodSpace,
    ResourceSpace,
    ResourceSpaceNoId,
    Saml2Sso,
    Saml2SsoPatch,
    Saml2SsoSp,
    Session,
    SmtpServer,
    SnapshotSpace,
    SnmpAgent,
    SnmpAgentPatch,
    SnmpManager,
    SnmpManagerPatch,
    Software,
    SoftwareBundle,
    SoftwareCheck,
    SoftwareInstallation,
    SoftwareInstallationStep,
    SoftwarePatch,
    Space,
    Subnet,
    SubnetPatch,
    SubscriptionAsset,
    Support,
    TestResultWithResource,
    TestResultWithResourceWithId,
    Vchost,
    VolumeCommon,
    VolumeGroup,
    VolumeGroupPatch,
    VolumeGroupPerformance,
    VolumeGroupPost,
    VolumePatch,
    VolumePerformance,
    VolumePost,
    VolumeSnapshot,
    VolumeSnapshotPatch,
    VolumeSnapshotPost,
    VolumeSnapshotTransfer,
    VolumeSpace,
    VolumeSpaceCommon,
    AdminPatch,
    ArrayPerformanceByLink,
    CertificatePost,
    LogTargetFile,
    PodPerformanceByArray,
    PolicyAuditFile,
    PolicyAuditFilePatch,
    PolicyNfs,
    PolicyNfsPatch,
    PolicySmb,
    PolicySmbPatch,
    ProtectionGroupSnapshotPatch,
    RemoteProtectionGroupSnapshotPost,
    ResourcePerformanceByArray,
    ResourcePerformanceNoIdByArray,
    SyslogServer,
    Volume,
    VolumeBatchPost
]

if os.environ.get('DOCS_GENERATION') is None:
    for model in CLASSES_TO_ADD_PROPS:
        add_properties(model)
