from __future__ import absolute_import
import os

from .client import Client
from ...exceptions import PureError
from ...properties import Property, Filter
from ...responses import ValidResponse, ErrorResponse, ApiError, ResponseHeaders

from .models.active_directory_post import ActiveDirectoryPost
from .models.admin_post import AdminPost
from .models.admin_settings import AdminSettings
from .models.aggregate_replication_performance import AggregateReplicationPerformance
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
from .models.arrayencryption_data_at_rest import ArrayencryptionDataAtRest
from .models.built_in import BuiltIn
from .models.built_in_relationship import BuiltInRelationship
from .models.built_in_resource_no_id import BuiltInResourceNoId
from .models.certificate_signing_request import CertificateSigningRequest
from .models.certificate_signing_request_post import CertificateSigningRequestPost
from .models.chap import Chap
from .models.cloud_provider_tag import CloudProviderTag
from .models.connection import Connection
from .models.connection_post import ConnectionPost
from .models.destroyed_patch_post import DestroyedPatchPost
from .models.directory_export import DirectoryExport
from .models.directory_export_post import DirectoryExportPost
from .models.directory_policy_export_post import DirectoryPolicyExportPost
from .models.directory_policy_post import DirectoryPolicyPost
from .models.directory_post import DirectoryPost
from .models.directory_quota import DirectoryQuota
from .models.directory_service_management import DirectoryServiceManagement
from .models.directory_service_role import DirectoryServiceRole
from .models.directory_snapshot_post import DirectorySnapshotPost
from .models.directorypolicyexportpost_policies import DirectorypolicyexportpostPolicies
from .models.directorypolicypost_policies import DirectorypolicypostPolicies
from .models.dns import Dns
from .models.dns_patch import DnsPatch
from .models.eradication_config import EradicationConfig
from .models.eula import Eula
from .models.eula_signature import EulaSignature
from .models.fixed_name_resource_no_id import FixedNameResourceNoId
from .models.fixed_reference import FixedReference
from .models.fixed_reference_no_id import FixedReferenceNoId
from .models.host_port_connectivity import HostPortConnectivity
from .models.host_post import HostPost
from .models.kmip_patch import KmipPatch
from .models.kmip_post import KmipPost
from .models.kmip_test_result import KmipTestResult
from .models.limited_by import LimitedBy
from .models.maintenance_window_post import MaintenanceWindowPost
from .models.member import Member
from .models.member_no_id_all import MemberNoIdAll
from .models.member_no_id_group import MemberNoIdGroup
from .models.network_interface_eth import NetworkInterfaceEth
from .models.network_interface_fc import NetworkInterfaceFc
from .models.network_interface_patch import NetworkInterfacePatch
from .models.network_interface_performance_eth import NetworkInterfacePerformanceEth
from .models.network_interface_performance_fc import NetworkInterfacePerformanceFc
from .models.networkinterfacepatch_eth import NetworkinterfacepatchEth
from .models.networkinterfacepost_eth import NetworkinterfacepostEth
from .models.new_name import NewName
from .models.offload_azure import OffloadAzure
from .models.offload_google_cloud import OffloadGoogleCloud
from .models.offload_nfs import OffloadNfs
from .models.offload_post import OffloadPost
from .models.offload_s3 import OffloadS3
from .models.override_check import OverrideCheck
from .models.page_info import PageInfo
from .models.performance import Performance
from .models.pod_performance_replication import PodPerformanceReplication
from .models.pod_replica_link_patch import PodReplicaLinkPatch
from .models.policy_member import PolicyMember
from .models.policy_member_export_post import PolicyMemberExportPost
from .models.policy_member_post import PolicyMemberPost
from .models.policy_post import PolicyPost
from .models.policy_rule_nfs_client import PolicyRuleNfsClient
from .models.policy_rule_nfs_client_post import PolicyRuleNfsClientPost
from .models.policy_rule_quota import PolicyRuleQuota
from .models.policy_rule_quota_post import PolicyRuleQuotaPost
from .models.policy_rule_smb_client import PolicyRuleSmbClient
from .models.policy_rule_smb_client_post import PolicyRuleSmbClientPost
from .models.policy_rule_snapshot import PolicyRuleSnapshot
from .models.policy_rule_snapshot_post import PolicyRuleSnapshotPost
from .models.policymemberexportpost_members import PolicymemberexportpostMembers
from .models.policymemberpost_members import PolicymemberpostMembers
from .models.policyrulenfsclientpost_rules import PolicyrulenfsclientpostRules
from .models.policyrulequotapost_rules import PolicyrulequotapostRules
from .models.policyrulesmbclientpost_rules import PolicyrulesmbclientpostRules
from .models.policyrulesnapshotpost_rules import PolicyrulesnapshotpostRules
from .models.port_common import PortCommon
from .models.port_initiator import PortInitiator
from .models.protection_group_target import ProtectionGroupTarget
from .models.qos import Qos
from .models.reference import Reference
from .models.reference_no_id import ReferenceNoId
from .models.replica_link_lag import ReplicaLinkLag
from .models.replica_link_performance_replication import ReplicaLinkPerformanceReplication
from .models.replication_performance_with_total import ReplicationPerformanceWithTotal
from .models.resource import Resource
from .models.resource_fixed_non_unique_name import ResourceFixedNonUniqueName
from .models.resource_no_id import ResourceNoId
from .models.retention_policy import RetentionPolicy
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
from .models.software_installation_patch import SoftwareInstallationPatch
from .models.software_installation_post import SoftwareInstallationPost
from .models.software_installation_steps_checks import SoftwareInstallationStepsChecks
from .models.software_upgrade_plan import SoftwareUpgradePlan
from .models.space import Space
from .models.start_end_time import StartEndTime
from .models.subnet_post import SubnetPost
from .models.support_patch import SupportPatch
from .models.support_remote_assist_paths import SupportRemoteAssistPaths
from .models.syslog_server_settings import SyslogServerSettings
from .models.tag import Tag
from .models.target_protection_group import TargetProtectionGroup
from .models.target_protection_group_post_patch import TargetProtectionGroupPostPatch
from .models.test_result import TestResult
from .models.throttle import Throttle
from .models.time_window import TimeWindow
from .models.transfer import Transfer
from .models.username import Username
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
from .models.array_connection_path import ArrayConnectionPath
from .models.array_factory_reset_token import ArrayFactoryResetToken
from .models.array_performance import ArrayPerformance
from .models.array_space import ArraySpace
from .models.arrays import Arrays
from .models.audit import Audit
from .models.certificate import Certificate
from .models.controller import Controller
from .models.directory import Directory
from .models.directory_patch import DirectoryPatch
from .models.directory_performance import DirectoryPerformance
from .models.directory_service import DirectoryService
from .models.directory_snapshot import DirectorySnapshot
from .models.directory_snapshot_patch import DirectorySnapshotPatch
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
from .models.kmip import Kmip
from .models.maintenance_window import MaintenanceWindow
from .models.network_interface import NetworkInterface
from .models.network_interface_performance import NetworkInterfacePerformance
from .models.network_interface_post import NetworkInterfacePost
from .models.offload import Offload
from .models.pod import Pod
from .models.pod_array_status import PodArrayStatus
from .models.pod_patch import PodPatch
from .models.pod_performance_replication import PodPerformanceReplication
from .models.pod_performance_replication_by_array import PodPerformanceReplicationByArray
from .models.pod_post import PodPost
from .models.pod_replica_link import PodReplicaLink
from .models.pod_replica_link_lag import PodReplicaLinkLag
from .models.pod_replica_link_performance_replication import PodReplicaLinkPerformanceReplication
from .models.pod_space import PodSpace
from .models.policy import Policy
from .models.policy_member_export import PolicyMemberExport
from .models.policy_patch import PolicyPatch
from .models.policy_smb_post import PolicySmbPost
from .models.port import Port
from .models.protection_group import ProtectionGroup
from .models.protection_group_performance import ProtectionGroupPerformance
from .models.protection_group_performance_array import ProtectionGroupPerformanceArray
from .models.protection_group_snapshot import ProtectionGroupSnapshot
from .models.protection_group_snapshot_post import ProtectionGroupSnapshotPost
from .models.protection_group_snapshot_transfer import ProtectionGroupSnapshotTransfer
from .models.reference_with_type import ReferenceWithType
from .models.remote_pod import RemotePod
from .models.remote_protection_group import RemoteProtectionGroup
from .models.remote_protection_group_snapshot import RemoteProtectionGroupSnapshot
from .models.remote_protection_group_snapshot_post import RemoteProtectionGroupSnapshotPost
from .models.remote_protection_group_snapshot_transfer import RemoteProtectionGroupSnapshotTransfer
from .models.remote_volume_snapshot import RemoteVolumeSnapshot
from .models.remote_volume_snapshot_transfer import RemoteVolumeSnapshotTransfer
from .models.replication_schedule import ReplicationSchedule
from .models.resource_performance import ResourcePerformance
from .models.resource_performance_no_id import ResourcePerformanceNoId
from .models.resource_pod_space import ResourcePodSpace
from .models.resource_space import ResourceSpace
from .models.resource_space_no_id import ResourceSpaceNoId
from .models.session import Session
from .models.smtp_server import SmtpServer
from .models.snmp_agent import SnmpAgent
from .models.snmp_agent_patch import SnmpAgentPatch
from .models.snmp_manager import SnmpManager
from .models.snmp_manager_patch import SnmpManagerPatch
from .models.software import Software
from .models.software_bundle import SoftwareBundle
from .models.software_installation import SoftwareInstallation
from .models.software_installation_step import SoftwareInstallationStep
from .models.space import Space
from .models.subnet import Subnet
from .models.subnet_patch import SubnetPatch
from .models.support import Support
from .models.syslog_server import SyslogServer
from .models.test_result_with_resource import TestResultWithResource
from .models.volume_common import VolumeCommon
from .models.volume_group import VolumeGroup
from .models.volume_group_performance import VolumeGroupPerformance
from .models.volume_group_post import VolumeGroupPost
from .models.volume_patch import VolumePatch
from .models.volume_performance import VolumePerformance
from .models.volume_post import VolumePost
from .models.volume_snapshot import VolumeSnapshot
from .models.volume_snapshot_patch import VolumeSnapshotPatch
from .models.volume_snapshot_post import VolumeSnapshotPost
from .models.volume_snapshot_transfer import VolumeSnapshotTransfer
from .models.admin_patch import AdminPatch
from .models.certificate_post import CertificatePost
from .models.policy_smb import PolicySmb
from .models.policy_smb_patch import PolicySmbPatch
from .models.protection_group_snapshot_patch import ProtectionGroupSnapshotPatch
from .models.resource_performance_by_array import ResourcePerformanceByArray
from .models.resource_performance_no_id_by_array import ResourcePerformanceNoIdByArray
from .models.volume import Volume


def add_properties(model):
    for name, value in model.attribute_map.items():
        setattr(model, name, Property(value))


CLASSES_TO_ADD_PROPS = [
    ActiveDirectoryPost,
    AdminPost,
    AdminSettings,
    AggregateReplicationPerformance,
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
    ArrayencryptionDataAtRest,
    BuiltIn,
    BuiltInRelationship,
    BuiltInResourceNoId,
    CertificateSigningRequest,
    CertificateSigningRequestPost,
    Chap,
    CloudProviderTag,
    Connection,
    ConnectionPost,
    DestroyedPatchPost,
    DirectoryExport,
    DirectoryExportPost,
    DirectoryPolicyExportPost,
    DirectoryPolicyPost,
    DirectoryPost,
    DirectoryQuota,
    DirectoryServiceManagement,
    DirectoryServiceRole,
    DirectorySnapshotPost,
    DirectorypolicyexportpostPolicies,
    DirectorypolicypostPolicies,
    Dns,
    DnsPatch,
    EradicationConfig,
    Eula,
    EulaSignature,
    FixedNameResourceNoId,
    FixedReference,
    FixedReferenceNoId,
    HostPortConnectivity,
    HostPost,
    KmipPatch,
    KmipPost,
    KmipTestResult,
    LimitedBy,
    MaintenanceWindowPost,
    Member,
    MemberNoIdAll,
    MemberNoIdGroup,
    NetworkInterfaceEth,
    NetworkInterfaceFc,
    NetworkInterfacePatch,
    NetworkInterfacePerformanceEth,
    NetworkInterfacePerformanceFc,
    NetworkinterfacepatchEth,
    NetworkinterfacepostEth,
    NewName,
    OffloadAzure,
    OffloadGoogleCloud,
    OffloadNfs,
    OffloadPost,
    OffloadS3,
    OverrideCheck,
    PageInfo,
    Performance,
    PodPerformanceReplication,
    PodReplicaLinkPatch,
    PolicyMember,
    PolicyMemberExportPost,
    PolicyMemberPost,
    PolicyPost,
    PolicyRuleNfsClient,
    PolicyRuleNfsClientPost,
    PolicyRuleQuota,
    PolicyRuleQuotaPost,
    PolicyRuleSmbClient,
    PolicyRuleSmbClientPost,
    PolicyRuleSnapshot,
    PolicyRuleSnapshotPost,
    PolicymemberexportpostMembers,
    PolicymemberpostMembers,
    PolicyrulenfsclientpostRules,
    PolicyrulequotapostRules,
    PolicyrulesmbclientpostRules,
    PolicyrulesnapshotpostRules,
    PortCommon,
    PortInitiator,
    ProtectionGroupTarget,
    Qos,
    Reference,
    ReferenceNoId,
    ReplicaLinkLag,
    ReplicaLinkPerformanceReplication,
    ReplicationPerformanceWithTotal,
    Resource,
    ResourceFixedNonUniqueName,
    ResourceNoId,
    RetentionPolicy,
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
    SoftwareInstallationPatch,
    SoftwareInstallationPost,
    SoftwareInstallationStepsChecks,
    SoftwareUpgradePlan,
    Space,
    StartEndTime,
    SubnetPost,
    SupportPatch,
    SupportRemoteAssistPaths,
    SyslogServerSettings,
    Tag,
    TargetProtectionGroup,
    TargetProtectionGroupPostPatch,
    TestResult,
    Throttle,
    TimeWindow,
    Transfer,
    Username,
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
    ArrayConnectionPath,
    ArrayFactoryResetToken,
    ArrayPerformance,
    ArraySpace,
    Arrays,
    Audit,
    Certificate,
    Controller,
    Directory,
    DirectoryPatch,
    DirectoryPerformance,
    DirectoryService,
    DirectorySnapshot,
    DirectorySnapshotPatch,
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
    Kmip,
    MaintenanceWindow,
    NetworkInterface,
    NetworkInterfacePerformance,
    NetworkInterfacePost,
    Offload,
    Pod,
    PodArrayStatus,
    PodPatch,
    PodPerformanceReplication,
    PodPerformanceReplicationByArray,
    PodPost,
    PodReplicaLink,
    PodReplicaLinkLag,
    PodReplicaLinkPerformanceReplication,
    PodSpace,
    Policy,
    PolicyMemberExport,
    PolicyPatch,
    PolicySmbPost,
    Port,
    ProtectionGroup,
    ProtectionGroupPerformance,
    ProtectionGroupPerformanceArray,
    ProtectionGroupSnapshot,
    ProtectionGroupSnapshotPost,
    ProtectionGroupSnapshotTransfer,
    ReferenceWithType,
    RemotePod,
    RemoteProtectionGroup,
    RemoteProtectionGroupSnapshot,
    RemoteProtectionGroupSnapshotPost,
    RemoteProtectionGroupSnapshotTransfer,
    RemoteVolumeSnapshot,
    RemoteVolumeSnapshotTransfer,
    ReplicationSchedule,
    ResourcePerformance,
    ResourcePerformanceNoId,
    ResourcePodSpace,
    ResourceSpace,
    ResourceSpaceNoId,
    Session,
    SmtpServer,
    SnmpAgent,
    SnmpAgentPatch,
    SnmpManager,
    SnmpManagerPatch,
    Software,
    SoftwareBundle,
    SoftwareInstallation,
    SoftwareInstallationStep,
    Space,
    Subnet,
    SubnetPatch,
    Support,
    SyslogServer,
    TestResultWithResource,
    VolumeCommon,
    VolumeGroup,
    VolumeGroupPerformance,
    VolumeGroupPost,
    VolumePatch,
    VolumePerformance,
    VolumePost,
    VolumeSnapshot,
    VolumeSnapshotPatch,
    VolumeSnapshotPost,
    VolumeSnapshotTransfer,
    AdminPatch,
    CertificatePost,
    PolicySmb,
    PolicySmbPatch,
    ProtectionGroupSnapshotPatch,
    ResourcePerformanceByArray,
    ResourcePerformanceNoIdByArray,
    Volume
]

if os.environ.get('DOCS_GENERATION') is None:
    for model in CLASSES_TO_ADD_PROPS:
        add_properties(model)
