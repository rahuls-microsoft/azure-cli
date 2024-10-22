# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools   
# The fleet parameters are set in the Az cmd as -
#  az azure-fleet fleet create --resource-group rgazurefleet --fleet-name testFleet --spot-priority-profile "{capacity:20,min-capacity:10,max-price-per-vm:0.00865,eviction-policy:Delete,allocation-strategy:PriceCapacityOptimized,maintain:True}" --regular-priority-profile "{capacity:20,min-capacity:10,allocation-strategy:LowestPrice}" --vm-sizes-profile "[{name:Standard_d1_v2,rank:19225}]" --compute-profile "{base-virtual-machine-profile:{osProfile:{computerNamePrefix:o,adminUsername:nrgzqciiaaxjrqldbmjbqkyhntp,adminPassword:adfbrdxpv,customData:xjjib,windowsConfiguration:{provisionVMAgent:True,enableAutomaticUpdates:True,timeZone:hlyjiqcfksgrpjrct,additionalUnattendContent:[{passName:OobeSystem,componentName:Microsoft-Windows-Shell-Setup,settingName:AutoLogon,content:bubmqbxjkj}],patchSettings:{patchMode:Manual,enableHotpatching:True,assessmentMode:ImageDefault,automaticByPlatformSettings:{rebootSetting:Unknown,bypassPlatformSafetyChecksOnUserSchedule:True}},winRM:{listeners:[{protocol:Https,certificateUrl:'https://myVaultName.vault.azure.net/secrets/myCertName'}]},enableVMAgentPlatformUpdates:True},linuxConfiguration:{disablePasswordAuthentication:True,ssh:{publicKeys:[{path:kmqz,keyData:kivgsubusvpprwqaqpjcmhsv}]},provisionVMAgent:True,patchSettings:{patchMode:ImageDefault,assessmentMode:ImageDefault,automaticByPlatformSettings:{rebootSetting:Unknown,bypassPlatformSafetyChecksOnUserSchedule:True}},enableVMAgentPlatformUpdates:True},secrets:[{sourceVault:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}'},vaultCertificates:[{certificateUrl:'https://myVaultName.vault.azure.net/secrets/myCertName',certificateStore:nlxrwavpzhueffxsshlun}]}],allowExtensionOperations:True,requireGuestProvisionSignal:True},storageProfile:{imageReference:{publisher:mqxgwbiyjzmxavhbkd,offer:isxgumkarlkomp,sku:eojmppqcrnpmxirtp,version:wvpcqefgtmqdgltiuz,sharedGalleryImageId:kmkgihoxwlawuuhcinfirktdwkmx,communityGalleryImageId:vlqe,id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{imageName}/versions/{versionName}'},osDisk:{name:wfttw,caching:None,writeAcceleratorEnabled:True,createOption:FromImage,diffDiskSettings:{option:Local,placement:CacheDisk},diskSizeGB:14,osType:Windows,image:{uri:'https://myStorageAccountName.blob.core.windows.net/myContainerName/myVhdName.vhd'},vhdContainers:[tkzcwddtinkfpnfklatw],managedDisk:{storageAccountType:Standard_LRS,diskEncryptionSet:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{diskEncryptionSetName}'},securityProfile:{securityEncryptionType:VMGuestStateOnly,diskEncryptionSet:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{diskEncryptionSetName}'}}},deleteOption:Delete},dataDisks:[{name:eogiykmdmeikswxmigjws,lun:14,caching:None,writeAcceleratorEnabled:True,createOption:FromImage,diskSizeGB:6,managedDisk:{storageAccountType:Standard_LRS,diskEncryptionSet:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{diskEncryptionSetName}'},securityProfile:{securityEncryptionType:VMGuestStateOnly,diskEncryptionSet:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{diskEncryptionSetName}'}}},diskIOPSReadWrite:27,diskMBpsReadWrite:2,deleteOption:Delete}],diskControllerType:uzb},networkProfile:{healthProbe:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/loadBalancers/{loadBalancerName}/probes/{probeName}'},networkInterfaceConfigurations:[{name:i,properties:{primary:True,enableAcceleratedNetworking:True,disableTcpStateTracking:True,enableFpga:True,networkSecurityGroup:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkSecurityGroups/{networkSecurityGroupName}'},dnsSettings:{dnsServers:[nxmmfolhclsesu]},ipConfigurations:[{name:oezqhkidfhyywlfzwuotilrpbqnjg,properties:{subnet:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName}'},primary:True,publicIPAddressConfiguration:{name:fvpqf,properties:{idleTimeoutInMinutes:9,dnsSettings:{domainNameLabel:ukrddzvmorpmfsczjwtbvp,domainNameLabelScope:TenantReuse},ipTags:[{ipTagType:sddgsoemnzgqizale,tag:wufmhrjsakbiaetyara}],publicIPPrefix:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPPrefixes/{publicIPPrefixName}'},publicIPAddressVersion:IPv4,deleteOption:Delete},sku:{name:Basic,tier:Regional}},privateIPAddressVersion:IPv4,applicationGatewayBackendAddressPools:[{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName}/backendAddressPools/{backendAddressPoolName}'}],applicationSecurityGroups:[{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationSecurityGroups/{applicationSecurityGroupName}'}],loadBalancerBackendAddressPools:[{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/loadBalancers/{loadBalancerName}/backendAddressPools/{backendAddressPoolName}'}],loadBalancerInboundNatPools:[{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/loadBalancers/{loadBalancerName}/inboundNatPools/{inboundNatPoolName}'}]}}],enableIPForwarding:True,deleteOption:Delete,auxiliaryMode:None,auxiliarySku:None}}],networkApiVersion:2020-11-01},securityProfile:{uefiSettings:{secureBootEnabled:True,vTpmEnabled:True},encryptionAtHost:True,securityType:TrustedLaunch,encryptionIdentity:{userAssignedIdentityResourceId:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{userAssignedIdentityName}'},proxyAgentSettings:{enabled:True,mode:Audit,keyIncarnationId:20}},diagnosticsProfile:{bootDiagnostics:{enabled:True,storageUri:'http://myStorageAccountName.blob.core.windows.net'}},extensionProfile:{extensions:[{name:bndxuxx,properties:{forceUpdateTag:yhgxw,publisher:kpxtirxjfprhs,type:pgjilctjjwaa,typeHandlerVersion:zevivcoilxmbwlrihhhibq,autoUpgradeMinorVersion:True,enableAutomaticUpgrade:True,settings:{},protectedSettings:{},provisionAfterExtensions:[nftzosroolbcwmpupujzqwqe],suppressFailures:True,protectedSettingsFromKeyVault:{secretUrl:'https://myvaultName.vault.azure.net/secrets/secret/mySecretName',sourceVault:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}'}}}}],extensionsTimeBudget:mbhjahtdygwgyszdwjtvlvtgchdwil},licenseType:v,scheduledEventsProfile:{terminateNotificationProfile:{notBeforeTimeout:iljppmmw,enable:True},osImageNotificationProfile:{notBeforeTimeout:olbpadmevekyczfokodtfprxti,enable:True}},userData:s,capacityReservation:{capacityReservationGroup:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}'}},applicationProfile:{galleryApplications:[{tags:eyrqjbib,order:5,packageReferenceId:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{applicationName}/versions/{versionName}',configurationReference:ulztmiavpojpbpbddgnuuiimxcpau,treatFailureAsDeploymentFailure:True,enableAutomaticUpgrade:True}]},hardwareProfile:{vmSizeProperties:{vCPUsAvailable:16,vCPUsPerCore:23}},serviceArtifactReference:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/serviceArtifacts/{serviceArtifactsName}/vmArtifactsProfiles/{vmArtifactsProfileName}'},securityPostureReference:{id:'/CommunityGalleries/{communityGalleryName}/securityPostures/{securityPostureName}/versions/{major.minor.patch}|{major.*}|latest',excludeExtensions:['{securityPostureVMExtensionName}'],isOverridable:True}},compute-api-version:2023-07-01,platform-fault-domain-count:1}" --zones "[zone1,zone2]" --identity "{type:UserAssigned,user-assigned-identities:{key9851:{}}}" --tags "{key3518:luvrnuvsgdpbuofdskkcoqhfh}" --location westus --plan "{name:jwgrcrnrtfoxn,publisher:iozjbiqqckqm,product:cgopbyvdyqikahwyxfpzwaqk,promotion-code:naglezezplcaruqogtxnuizslqnnbr,version:wa}"
# --------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------
"""
Test suite for the Azure Compute Fleet CLI commands.
This module contains tests for creating, updating, showing, deleting, listing, scaling, and restarting compute fleets using the Azure CLI.
Classes:
    TestComputefleetScenario: Contains test methods for various compute fleet operations.
Methods:
    __init__(self, method_name): Initializes the test scenario.
    test_fleet_create(self): Tests the creation of a compute fleet.
    test_fleet_update(self): Tests updating a compute fleet's tags.
    test_fleet_show(self): Tests showing details of a compute fleet.
    test_fleet_delete(self): Tests deleting a compute fleet.
    test_fleet_list(self): Tests listing all compute fleets in a resource group.
    test_fleet_scale(self): Tests scaling a compute fleet's capacity.
    test_fleet_restart(self): Tests restarting a compute fleet.
    """
# --------------------------------------------------------------------------------------------

import os
import unittest
import json

from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk.scenario_tests import AllowLargeResponse, record_only
import random
import string
from fleet_test_helper import ComputefleetHelper  # Ensure this import points to the correct module

defaultSubscription = 'ac302a10-6fb1-4308-baf6-ad855c4d7f3d'
subscriptionId = os.getenv('AZURE_SUBSCRIPTION_ID')
if not subscriptionId:
    subscriptionId = defaultSubscription

fleet_name = 'testFleet'

def generate_random_rg_name(prefix='test_fleet_cli_rg_', length=8):
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return prefix + suffix

resource_group = generate_random_rg_name()
location = "eastus"

class TestComputefleetScenario(ScenarioTest):

    @classmethod
    def setUpClass(cls):
        super(TestComputefleetScenario, cls).setUpClass()
        cls.resource_group = resource_group
        cls.location = location
        cls.create_resource_group()

    @classmethod
    def tearDownClass(cls):
        cls.delete_resource_group()
        super(TestComputefleetScenario, cls).tearDownClass()

    @classmethod
    def create_resource_group(cls):
        instance = cls('test_fleet_create')
        instance.cmd('az group create --name {} --location {}'.format(cls.resource_group, cls.location))

    @classmethod
    def delete_resource_group(cls):
        instance = cls('test_fleet_create')
        instance.cmd('az group delete --name {} --yes --no-wait'.format(cls.resource_group))

    def generate_fleet_parameters(self, subscription_id, resource_group, location):
        public_ip_address_id = self.create_public_ip_address(subscription_id, resource_group, location)
        # Use the ComputefleetHelper to generate fleet parameters
        return ComputefleetHelper.generate_fleet_parameters(self, subscription_id, resource_group, location, public_ip_address_id)
      
    def create_public_ip_address(self,  subscriptionId, resourceGroupName, location):
        public_ip_address_name = self.create_random_name('testFleetPublicIP-', 24)
        public_ip_address_id = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPAddresses/{public_ip_address_name}"
        input_data = {
            "location": location,
            "sku": {"name": "Standard"},
            "properties": {
                "publicIPAllocationMethod": "Static"
            }
        }
        
        input_data_json = json.dumps(input_data)
        properties = '"{input_data_json}"'
        self.kwargs.update({
            'public_ip_address_id': public_ip_address_id,
            'input_data_json': input_data_json,
            'location': location,
            'ip_properties': properties,
            'resource_group': resourceGroupName,
            'public_ip_address_name': public_ip_address_name
        })
        
        self.cmd('az network public-ip create --name {public_ip_address_name} --resource-group {resource_group} --allocation-method Static --sku Standard --location {location} --sku Standard ')
        return public_ip_address_id
    
    @AllowLargeResponse()
    def test_fleet_create(self, fleet=fleet_name, rg=resource_group, loc=location):
        fleetData = self.generate_fleet_parameters(subscriptionId, rg, loc)
        fleetData_json = json.dumps(fleetData)
        print(fleetData_json)
        
        self.kwargs.update({
            'fleet_name': fleet,
            'resource_group': rg,
            'location': loc,
            'fleet_data_json': fleetData_json
        })

        self.cmd('az computefleet create --name {fleet_name} --resource-group {resource_group} --spot-priority-profile {fleet_data_json}', checks=[
            self.check('name', '{fleet_name}'),
            self.check('resourceGroup', '{resource_group}')
        ])

    def test_fleet_update(self, fleet=fleet_name, rg=resource_group):
        self.kwargs.update({
            'fleet_name': fleet,
            'resource_group': rg,
            'new_tag': 'newTag'
        })

        self.cmd('az computefleet update --name {fleet_name} --resource-group {resource_group} --set tags.key={new_tag}', checks=[
            self.check('tags.key', '{new_tag}')
        ])

    def test_fleet_show(self, fleet=fleet_name, rg=resource_group):
        self.kwargs.update({
            'fleet_name': fleet,
            'resource_group': rg
        })

        self.cmd('az computefleet show --name {fleet_name} --resource-group {resource_group}', checks=[
            self.check('name', '{fleet_name}'),
            self.check('resourceGroup', '{resource_group}')
        ])

    @AllowLargeResponse()
    def test_fleet_list(self, rg=resource_group):
        self.kwargs.update({
            'resource_group': rg
        })

        self.cmd('az computefleet list --resource-group {resource_group}', checks=[
            self.check('type(@)', 'array'),
            self.check('length(@)', 1)
        ])

    def test_fleet_scale(self, fleet=fleet_name, rg=resource_group):
        self.kwargs.update({
            'fleet_name': fleet,
            'resource_group': rg,
            'new_capacity': 5
        })

        self.cmd('az computefleet scale --name {fleet_name} --resource-group {resource_group} --capacity {new_capacity}', checks=[
            self.check('capacity', '{new_capacity}')
        ])

    def test_fleet_restart(self, fleet=fleet_name, rg=resource_group):
        self.kwargs.update({
            'fleet_name': fleet,
            'resource_group': rg
        })

        self.cmd('az computefleet restart --name {fleet_name} --resource-group {resource_group}', checks=[
            self.check('status', 'Succeeded')
        ])

    def test_fleet_delete(self, fleet=fleet_name, rg=resource_group):
        self.kwargs.update({
            'fleet_name': fleet,
            'resource_group': rg
        })

        self.cmd('az computefleet delete --name {fleet_name} --resource-group {resource_group}', checks=[
            self.is_empty()
        ])
  
    @AllowLargeResponse()
    @record_only()
    def test_all_fleet_operations(self):
        self.test_fleet_create()
        self.test_fleet_update()
        self.test_fleet_show()
        self.test_fleet_scale()
        self.test_fleet_restart()
        self.test_fleet_delete()

if __name__ == '__main__':
    unittest.main()