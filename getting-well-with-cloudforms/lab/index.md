# Lab Introduction

<!-- TOC -->

- [Lab Introduction](#lab-introduction)
    - [Introduction to CloudForms](#introduction-to-cloudforms)
        - [Access the lab environment](#access-the-lab-environment)
    - [Verify Lab](#verify-lab)
        - [OpenStack Provider status](#openstack-provider-status)
        - [Red Hat Virtualization Provider status](#red-hat-virtualization-provider-status)
        - [vCenter Provider status](#vcenter-provider-status)
    - [Build a Service Catalog with CloudForms](#build-a-service-catalog-with-cloudforms)
        - [What's the value of having a service catalog?](#whats-the-value-of-having-a-service-catalog)
        - [Service Basics](#service-basics)
        - [Virtual Machine Provisioning example](#virtual-machine-provisioning-example)
        - [Build a VM Provisioning Service Dialog](#build-a-vm-provisioning-service-dialog)
        - [Build a VM Provisioning Service Catalog](#build-a-vm-provisioning-service-catalog)
        - [Build a Virtual Machine Service Catalog Item](#build-a-virtual-machine-service-catalog-item)
        - [Order the Simple Virtual Machine Service Catalog Item](#order-the-simple-virtual-machine-service-catalog-item)
        - [Verify the order](#verify-the-order)
        - [HEAT Provisioning example](#heat-provisioning-example)
        - [Prepare the HEAT Template](#prepare-the-heat-template)
        - [Import the HEAT Template](#import-the-heat-template)
        - [Create a Service Dialog from a HEAT template](#create-a-service-dialog-from-a-heat-template)
        - [Verify the Service Dialog](#verify-the-service-dialog)
        - [Build a HEAT Service Catalog](#build-a-heat-service-catalog)
        - [Build a HEAT Service Catalog Item](#build-a-heat-service-catalog-item)
        - [Order the HEAT Wordpress Catalog Item](#order-the-heat-wordpress-catalog-item)
        - [Verify provisioning in OpenStack](#verify-provisioning-in-openstack)
    - [CloudForms 4.5 with Ansible batteries included](#cloudforms-45-with-ansible-batteries-included)
        - [Introduction to Ansible](#introduction-to-ansible)
        - [Make sure embedded Ansible role is enabled and running](#make-sure-embedded-ansible-role-is-enabled-and-running)
        - [Add a Git repository of Ansible Playbooks](#add-a-git-repository-of-ansible-playbooks)
        - [Add vCenter credentials](#add-vcenter-credentials)
        - [Verify repository sync](#verify-repository-sync)
        - [Install pysphere](#install-pysphere)
        - [Build a Service Catalog to create and delete users](#build-a-service-catalog-to-create-and-delete-users)
        - [Create a Service Catalog for Ansible Playbooks](#create-a-service-catalog-for-ansible-playbooks)
        - [Create a Service Catalog Item for the Playbook](#create-a-service-catalog-item-for-the-playbook)
        - [Order the "create user" Service Catalog Item](#order-the-create-user-service-catalog-item)
        - [Monitor create user Playbook execution](#monitor-create-user-playbook-execution)
        - [Verify Playbook results](#verify-playbook-results)
        - [Build a Service Catalog to deploy Virtual Machines](#build-a-service-catalog-to-deploy-virtual-machines)
        - [Order the Virtual Machine Provisioning Service Catalog Item](#order-the-virtual-machine-provisioning-service-catalog-item)
        - [Monitor VM provisioning Playbook execution](#monitor-vm-provisioning-playbook-execution)
        - [Extend CloudForms builtin Capabilities](#extend-cloudforms-builtin-capabilities)
        - [Add a Git repository for Automate](#add-a-git-repository-for-automate)
        - [Verify Automate import](#verify-automate-import)
        - [Optimize the Dialog](#optimize-the-dialog)
        - [Update the Service Catalog Item](#update-the-service-catalog-item)
        - [Test the new Service Dialog](#test-the-new-service-dialog)
    - [Policies and Ansible](#policies-and-ansible)
        - [Creating the Service](#creating-the-service)
        - [Create a Service Catalog Item for the Playbook](#create-a-service-catalog-item-for-the-playbook-1)
        - [Creating Control Action](#creating-control-action)
        - [Create VM Control Policy](#create-vm-control-policy)
        - [Setting Event Assignment](#setting-event-assignment)
        - [Setting Control Action on Event](#setting-control-action-on-event)
        - [Creating and Assigning Policy Profile](#creating-and-assigning-policy-profile)
        - [Assign the policy profile](#assign-the-policy-profile)
        - [Testing the Policy Profile](#testing-the-policy-profile)
    - [Advanced labs](#advanced-labs)
        - [Use the Self Service user Interface](#use-the-self-service-user-interface)
        - [Use role Based Access Control to publish Service Catalog](#use-role-based-access-control-to-publish-service-catalog)
        - [User Groups](#user-groups)
        - [Roles](#roles)
        - [More details](#more-details)
        - [Create a Role](#create-a-role)
        - [Create a new Group](#create-a-new-group)
        - [Create a new User](#create-a-new-user)
        - [Test user Joe Doe](#test-user-joe-doe)
        - [Grant access to certain Catalog Items](#grant-access-to-certain-catalog-items)
        - [Test once more as Joe Doe](#test-once-more-as-joe-doe)
    - [Even more?](#even-more)

<!-- /TOC -->

## Introduction to CloudForms

[General introduction](../../common/index.md)

### Access the lab environment

Navigate to the RHPDS Portal and order the "Getting Well With CloudForms" in the catalog "Cloud Infrastructure Demos".

[https://rhpds.redhat.com](https://rhpds.redhat.com)

If you've never used RHPDS before, make sure you follow the [Lab Environment Access Instructions](https://mojo.redhat.com/docs/DOC-1133834). In particular, request an account on the [OPENTLC Account Management Request Access](https://account.opentlc.com/account/requestAccessForm.php) page. If you only forgot your password, follow the instructions on the [OPENTLC Account Management](https://account.opentlc.com/account/) page.

After you logged in, navigate to ***Services*** -> ***Catalogs***. Open the "EMEA RHTE" Catalog.

![EMEA RHTE Catalog](img/emea-rhte-catalog.png) 

Click on the "EMEA RHTE CF Lab" and click on ***Order*** to start deployment. 

![Order CF Lab](img/order-rhte-lab.png)

***Note:*** Give the lab up to 15 minutes to complete provisioning!

You will receive an email with the list of all virtual machines which have been deployed as part of the lab. 

The lab is comprised of a number of systems:

- Red Hat CloudForms Management Engine

        URL: https://cf-<GUID>.rhpds.opentlc.com

        User: admin / password: r3dh4t1!

- Red Hat Enterprise Virtualization Manager

        URL: https://rhevm-<GUID>.rhpds.opentlc.com

        User: admin@internal / password: r3dh4t1!

- Red Hat OpenStack Platform

        URL: https://osp-<GUID>.rhpds.opentlc.com

        User: admin / password: r3dh4t1!

    ***Note:*** IF you don't use HTTPS when connecting to OpenStack Horizon, you will only see the Default Apache Welcome Page (no automatic redirect). Make sure you use HTTPS to access Horizon.

- VMware vCenter

        URL: https://vcenter-<GUID>.rhpds.opentlc.com

        User: root / password: r3dh4t1!

The ID &lt;GUID&gt; is unique to your lab environment.

***Note:*** Your browser might give you a warning message about the used SSL Certificates. These warning messages can be accepted and are due to the fact that each lab deployed with new certificates on request.

## Verify Lab

### OpenStack Provider status

Let's first check the OpenStack Provider:

1. Navigate to ***Compute*** -> ***Clouds*** -> ***Providers***

    ![navigate to cloud providers](img/navigate-to-compute-clouds-providers.png)

1. You should see a tile icon labeled "RHEV". Click on it.

    ![OpenStack provider tile icon](img/openstack-provider-tile.png)

1. Click on ***Authentication*** -> ***Re-check Authentication Status***

    ![re-check authentication](img/openstack-recheck-authentication.png)

This will validate the credentials are correct, and it will also restart the provider specific background processes.

After reloading the page, the provider tile should show a green check mark and the last update fields should report "less than a minute ago".

### Red Hat Virtualization Provider status

Let's then check the RHV Provider:

1. Navigate to ***Compute*** -> ***Infrastructure*** -> ***Providers***

    ![navigate to cloud providers](img/navigate-to-compute-infrastructure-providers.png)

1. You should see a tile icon labeled "OpenStack". Click on it.

    ![OpenStack provider tile icon](img/rhv-provider-tile.png)

1. Click on ***Authentication*** -> ***Re-check Authentication Status***

    ![re-check authentication](img/rhv-recheck-authentication.png)

This will validate the credentials are correct, and it will also restart the provider specific background processes.

### vCenter Provider status

Last but not least, let's check the vCenter Provider:

1. Navigate to ***Compute*** -> ***Infrastructure*** -> ***Providers***

    ![navigate to cloud providers](img/navigate-to-compute-infrastructure-providers.png)

1. You should see a tile icon labeled "vCenter". Click on it.

    ![OpenStack provider tile icon](img/vcenter-provider-tile.png)

1. Click on ***Authentication*** -> ***Re-check Authentication Status***

    ![re-check authentication](img/vcenter-recheck-authentication.png)

This will validate the credentials are correct, and it will also restart the provider specific background processes.

1. Go back to ***Compute*** -> ***Infrastructure*** -> ***Providers***

    ![navigate to infrastructure providers](img/navigate-to-compute-infrastructure-providers.png)

1. Check all providers show a green check mark

    ![all providers healthy](img/all-providers-green.png)

1. Now you're ready to go!

## Build a Service Catalog with CloudForms

This lab will guide you through the process of creating a service catalog in CloudForms.

### What's the value of having a service catalog?

One of the features a Cloud Management Platform provides, is a self service user interface. Here users can order, manage and retire services. Services are categorized in catalogs, where they can be organized and easily consumed.

By providing a service catalog, users can deploy the services they need quickly and simply. This will improve agility, reduce provisioning time and free up resources in internal IT.

### Service Basics

But first some basics. Four items are required to make a service available to users from the CloudForms self service portal:

1. A Provisioning Dialog which presents the basic configuration options for a virtual machine or instance.
1. A Service Dialog where you allow users to configure virtual machine or instance options.
1. A Service Catalog which is used to group Services Catalog Items together.
1. A Service Catalog Item (the actual Service) which combines a Service Dialog, a Provisioning Dialog and some additional meta data in the Service Catalog.

We can also use Role Based Access Control to make certain Service Catalog Items available to specific groups of users.

### Virtual Machine Provisioning example

The first example will guide you through the process of offering a Service Catalog Item to provision a simple virtual machine. This will include:

- Design a Service Dialog: a form which will ask the user for the necessary input data
- Create a Service Catalog: this will allow to organize services in a structured way
- Publish a Service Catalog Item: puts everything together and build the item which users can order

The previous chapter mentions a fourth object, the Provisioning Dialog. We do not have to create one, since there are examples shipped with the product, which does everything we need.

The following chapters will guide you through the process step-by-step.

### Build a VM Provisioning Service Dialog

For this example we will create a Service Dialog which will ask the user for two parameters:

* the name of the new virtual machine
* how much memory should be allocated to the new virtual machine

Follow these steps to design the service dialog:

1. Navigate to ***Automation*** -> ***Automate*** -> ***Customization***

    ![navigate to Automation, Automate, Customization](img/navigate-to-customization.png)

1. Navigate to ***Service Dialogs*** in the accordion on the left.

    ![navigate to service dialogs](img/service-dialog-accordion.png)

1. Click on ***Configuration*** -> ***Add a new Dialog***

1. Chose a label and description:

    ***Label***: Simple VM

    ***Description***: Simple VM provisioning dialog

    ***Note:*** Make sure ***Submit*** and ***Cancel*** are both checked

    ***Note:*** Do not try to save the changes right now! The dialog is not finished and you will receive and error message ("Validation failed: Dialog Simple VM must have at least one Tab")

    ![create a service dialog](img/create-service-dialog.png)

1. Click on the little plus icon in the menu on the top and select ***Add a new Tab to this Dialog***

    Tabs can be used to make complex Service Dialogs easier to navigate and fill out. They are often used to logically structure related questions (e.g. "General Configuration", "Network Configuration", "user Configuration").

    For this lab, we will keep it simple:

    ***Label:*** Generic

    ***Description:*** Generic Tab

    ![add a new tab to the dialog](img/generic-tab.png)

1. Click on the little plus icon and ***Add a new Box to this Tab***

    Boxes are used to visually group related dialog elements. For example in the network configuration Service Dialog a box could be used to group all IPv4 related questions, and another box to group all IPv6 related questions.

    For this lab we create a simple box:

    ***Label:*** Generic

    ***Description:*** Generic Box

    ![add a new box to the tab](img/generic-box.png)

1. Now we can add elements to this box. Click on ***Add a new Element to this Box***

    The first element will allow the user to specify a VM name:

    The Label is the name of the element as it will be shown in the UI:

    ***Label:*** VM Name

    The name will be used for the internal variable of the provisioning workflow:

    ***Name:*** option_0_vm_name

    The description is some text which will be shown if the mouse pointer is hovering over this element. It can be used to provide additional information to the user to fill out this field:

    ***Description:*** Specify the name of the new virtual machine

    CloudForms allows us to design Service Dialogs comprised of many different types of Elements:
    
    - Check box: allows to user to check or uncheck the element, often used to ask for additional optional data
    - Date Control: allows the user to select a date from a calender widget. Often used for retirement or other date related options
    - Date/Time Control: same as Date Control, but also allows to specify a time, for example used to specify an automated shutdown or if a change should be scheduled for later
    - Drop Down List: allows the user to select one or multiple options from a list, for example to chose from a list of available networks, applications, cost centers and many more
    - Radio Button: Similar to the check box, but only one of the options can be selected, for example the base OS version (RHEL 6 or RHEL 7, but never more than one)
    - Tag Control: a special element which allows the user to chose from available tags. More about tagging later in this lab
    - Text Area Box: allows the user to enter relatively large amounts of text (multiple lines), could be used for example to provide description information
    - Text Box: allows the user for short amounts of text (one line), in this example we use this element to ask the user for a name of the virtual machine
    
    We want the user to enter a text which then will be used to name the VM. This can be accomplished by selecting "Text Box" in the ***Type*** drop down list.

    ![add a new element to ask for the VM name](img/element-vmname.png)

    The remaining options can be ignored for now.

1. We want to add a second element where the user can chose the memory size of the new VM. Click once more on ***Add a new Element to this Box***.

    ***Label:*** Memory size

    ***Name:*** option_0_vm_memory

    ***Description:*** Select how much memory the virtual machine should have

    ***Type:*** Drop Down List

    A element of type "Drop Down List" allows the user to select one of the predefined values. To create the list of selectable values, scroll down to the table "Entries" and add the following lines:

    ***Value:*** 2048

    ***Description:*** 2 GB

    ***Value:*** 4096

    ***Description:*** 4 GB

    ***Value:*** 8192

    ***Description:*** 8 GB

    ***Note:*** To be able to add a line to the table, click on the little "Add this entry" icon on the left of each row!

    ![add entries to the drop down list](img/memory-dropdownlist.png)

1. We are finally done designing the dialog. Click on ***Add*** to save the dialog.

    ***Note:*** If you're having trouble creating the Service Dialog, you can download it from [Github](https://raw.githubusercontent.com/cbolz/partner-conference-2017-labs/master/cloudforms-service-catalog-lab/service-dialog/simple-vm.yml) and import it. Follow the instructions on how to [import a service dialog](service-dialog-import.md) ONLY if you were unable to create the dialog.

### Build a VM Provisioning Service Catalog

The following steps will create a Service Catalog.

1. The next step is to create a Service Catalog. First we have to navigate to ***Services*** -> ***Catalogs***.

    ![navigate to services, catalog](img/navigate-to-service-catalog.png)

1. Click on ***Catalogs*** in the accordion on the left

    ![service catalogs](img/service-catalogs.png)

1. Click on ***Configuration*** and ***Add a New Catalog***

1. Fill out name and description:

    ***Name:*** Virtual Machines

    ***Description:*** Deploy Virtual Machines from the Catalog

    ![add a new catalog](img/add-a-new-catalog.png)

1. Click ***Add*** to save the Service Catalog

### Build a Virtual Machine Service Catalog Item

To tie everything together, the last step is to define a service catalog item.

1. Navigate to ***Services*** -> ***Catalogs***

    ![navigate to services, catalog](img/navigate-to-service-catalog.png)

1. Click on ***Catalog items*** in the accordion on the left.

    You should already see two Service Catalogs:

    ***Unassigned:*** Catalog items which are not published yet, will be listed here

    ***Virtual Machines:*** the Service Catalog we just created in the previous step

    ![navigate to catalog items](img/navigate-to-catalog-items.png)

1. In the ***Configuration*** Menu, click on ***Add a New Catalog Item***

    Catalog Bundles are used for multi tier applications and consist of many Catalog Items. Since we do not have any existing Catalog Items, we can not create a Bundle.

1. Chose the Catalog Item Type. For this example we want to use the Red Hat Virtualization Provider, so click on ***RHEV***

    ![select catalog item type](img/select-catalog-item-type.png)

    ***Note:*** It can take a few seconds for the next screen to load.

1. The next dialog will ask for the details of the new Service Catalog Item:

    The name of the Service Catalog Item shown in the UI:

    ***Name:*** Simple VM

    A more descriptive text about the Service Catalog Item:

    ***Description:*** A simple Linux Virtual Machine

    Check the "Display in Catalog" box. If not selected, the Service Catalog Item will not be visible to users. This can be used for Items which are either still in draft mode, or should only be ordered as a part of a bundle:

    ***Display in Catalog:*** check this box

    Select the previously created Service Catalog:

    ***Catalog:***  Virtual Machines

    Select the previously created Service Dialog:

    ***Dialog:*** Simple VM

    All other fields on this tab can remain unchanged.

    ![adding a new catalog item](img/adding-a-new-catalog-item.png)

    Entry Points are the hooks into CloudForms' powerful Automation Framework. It allows administrators to define provisioning, reconfiguration and retirement workflows which are different from the out of the box behavior. For example we could add integration into an IP Address Management Tool, a ticketing system or a CMDB Service. For this lab, we want to stick with the out of the box experience and leave those fields unchanged.

1. Click on the ***Details*** tab. You can provide some more descriptive explanation about the service here. We can even use basic HTML formatting in this box.

        <h1>Simple VM</h1>
        <p>When ordering this item, the user will be provided some simple questions to specify the hostname and memory size of the requested virtual machine.</p>

        <p>The VM will be deployed with <a href=http://www.redhat.com>Red Hat Enterprise Linux 7</a>.

1. The ***Request Info*** tab of the dialog allows us to provide all the settings we want to use when provisioning a virtual machine from this Service Catalog Item.

    Select the template used for provisioning:

    ***Selected VM:*** rhel73

    For automatic naming chose "changeme"

    ***Naming:*** changeme

    If no name is specified, this will cause CloudForms to automatically assign a name based on "cfme" as a prefix. The name will be expanded with a unique ID starting with 001.

1. Click on the sub tab ***Environment***

    Although it sounds the most convenient option, we can not use "Choose Automatically". This will require the definition of a provisioning scope, which we haven't done yet. Instead we we set the appropriate values manually.

    The datacenter of our Red Hat Virtualization Provider:

    ***Datacenter:*** Default

    The cluster in the Red Hat Virtualization Datacenter:

    ***Cluster:*** Default

    The host which will perform the actual tasks and where the VM will initially run on:

    ***Host:*** rhelkvm

    The storage domain to store the VM

    ***Datastore:*** vmstore00

1. Click on the next sub tab ***Hardware***

    For the purpose of the lab, the provided defaults are fine.

1. Click on the next sub tab ***Network***

    The lab environment is very simple, there is only one VLAN available:

    ***VLAN:*** rhevm

1. Click on the next sub tab ***Customize***

    This allows to reconfigure certain settings inside the virtual machine. For this lab, we keep them all empty

1. Click on the last sub tab ***Schedule***

    This allows us to delay provisioning to a later time, for example during the night or off hours. We can also set a retirement date. After notifying the user and allowing him or her to extend the lifespan of the virtual machine, retirement will shutdown and, by default, delete the virtual machine.

    For the purpose of the lab, we keep these settings unchanged.

1. Finally click on ***Add*** to save the Catalog Item

    ![catalog item saved](img/catalog-item-saved.png)

### Order the Simple Virtual Machine Service Catalog Item

For sure you want to test the Service Catalog Item you just created!

1. Navigate to ***Services*** -> ***Catalogs*** and then click on ***Service Catalogs*** in the accordion on the left.

    ![navigate to services, catalog](img/navigate-to-service-catalog.png)

1. You should see the Service Catalog Item we just created:

    ![all services](img/all-services.png)

1. Click on the Item to see more details.

    ![service item details](img/service-item-details.png)

    Note that the Link for Red Hat Enterprise Linux in fact opens the Red Hat Homepage.

1. Click on ***Order***

1. The Service Dialog we created earlier will be presented and ask for the name of the virtual machine and the memory size. As you can see, the name is a free text field, and the memory size is a drop down list.

    Chose an example virtual machine name and the amount of memory you would like to be allocated.

    ![example-oder-simple-vm](img/example-order-simple-vm.png)

1. You will be redirected to the request queue where you can see CloudForms working on your request.

    ![simple vm ordered](img/simple-vm-ordered.png)

    ***Note:*** Since we are using nested virtualization to run these labs, performance will be slow and it can take several minutes to complete the request (20-30 minutes).

### Verify the order

In the requests queue you can click on ***Reload*** to see how CloudForms processes the order. If you click the button a few times, you should see the status is progressing.

We want to log into Red Hat Virtualization to see how the virtual machine is created:

1. Open the Red Hat Virtualization Web UI in a new browser window or tab.

        URL: https://rhevm-<GUID>.rhpds.opentlc.com

    ![rhv portal page](img/rhv-portal.png)

1. Click on ***Administrator Portal***

    ![rhv admin portal](img/rhv-admin-portal.png)

1. Log in with these credentials:

        ***user:*** admin

        ***Password:*** r3dh4t1!

    Make sure the profile is set to "internal".

1. Click on the tab ***Virtual Machines*** to see all existing virtual machines

    ![vm overview](img/rhv-vm-overview.png)

1. After a few moments you're virtual machine should automatically show up in the list.

    ![lab VM showing up](img/rhv-lab-vm.png)

    Note that while the virtual machine is created, the memory size is still 1 GB. This value is specified in the template therefore copied when creating the virtual machine. Only after the virtual machine was successfully cloned, CloudForms corrects the memory size.

    ![lab VM complete](img/rhv-lab-vm-complete.png)

1. This concludes this first part of the lab

### HEAT Provisioning example

In the first part of the lab you have learned:

- how to design a Service Dialog
- how to create a Service Catalog
- put everything together with a Service Catalog Item
- order from the Service Catalog

In the second part of the lab, we want to use HEAT to create a new instance and to provision an application inside the instance. We are using the probably most popular example: [Wordpress](www.wordpress.org). The HEAT template we use, can be found in the [OpenStack Git Repository](https://github.com/openstack/heat-templates/blob/master/hot/F20/WordPress_Native.yaml).

In the previous lab, we had to create a Service Dialog manually. With HEAT, CloudFormations and Microsoft ARM Templates, CloudForms can automatically create a Service Dialog for us. We can still edit this automatically created Service Dialog, to adjust it to our needs.

### Prepare the HEAT Template

Before we can import the template into CloudForms, we need to download it or have it open in a separate browser window.

***Note:*** Please used the forked version of the HEAT Template, which has an additional field "Network" defined. Without this field, running the HEAT Template will fail with an error indicating that mulitple networks are available and hence a network has to be specified.

1. Go to the template on the Github project page.

    [https://github.com/cbolz/partner-conference-2017-labs/blob/master/cloudforms-service-catalog-lab/HEAT/WordPress_Native.yaml](https://github.com/cbolz/partner-conference-2017-labs/blob/master/cloudforms-service-catalog-lab/HEAT/WordPress_Native.yaml)

1. Make sure to open the file in "RAW" mode or use this link:
    [https://raw.githubusercontent.com/cbolz/partner-conference-2017-labs/master/cloudforms-service-catalog-lab/HEAT/WordPress_Native.yaml](https://raw.githubusercontent.com/cbolz/partner-conference-2017-labs/master/cloudforms-service-catalog-lab/HEAT/WordPress_Native.yaml)

1. Download the HEAT Template or open it in a separate browser window so you can copy and paste it into the CloudForms Web UI

### Import the HEAT Template

The following procedure will import a HEAT template, create a service dialog and tie everything together in a service catalog item.

1. Navigate to ***Services*** -> ***Catalogs***

    ![navigate to services catalogs](img/navigate-to-service-catalog.png)

1. Click on ***Orchestration Templates*** in the accordion on the left

    ![orchestration templates](img/orchestration-templates.png)

    You should see one existing templates which is provided by CloudForms out of the box. It's a special predefined template to provision virtual machines on Microsoft Azure.

1. Create a new Orchestration template by clicking on ***Configuration*** -> ***Create new Orchestration Template***

1. Give the template a name and description:

    ***Name:*** Wordpress HEAT Template

    ***Description:*** This template can be used to deploy a Wordpress instance on OpenStack

    ***Template Type:*** OpenStack Heat

    Copy and paste the HEAT Template you downloaded before into the large text area below those fields. Make sure you copy the entire HEAT template by opening the [RAW page](https://raw.githubusercontent.com/cbolz/partner-conference-2017-labs/master/cloudforms-service-catalog-lab/HEAT/WordPress_Native.yaml) of the file on Github.

    ![wordpress template](img/wordpress-heat-template.png)

    ***Note:*** The screenshot is truncated! Make sure you copy the entire HEAT Template! The first line should be:

        heat_template_version: 2013-05-23

    And the last line should be:

        host: { get_attr: [wordpress_instance, first_address] }

1. Click ***Add*** to save the orchestration template

    ![orchestration template saves](img/orchestration-template-saves.png)

### Create a Service Dialog from a HEAT template

Earlier in this lab you learned how to manually create a Service Dialog. Now we will see that CloudForms can do this work for us, if we use an orchestration template.

1. Navigate to the orchestration template you just created

1. Click on ***Configuration*** -> ***Create Service Dialog from Orchestration Template***

    ![create service dialog from wordpress heat template](img/create-service-dialog-from-wordpress.png)

1. Enter a name for the new Service Dialog

    ***Service Dialog Name:*** Wordpress HEAT Template

    ![create service dialog from orchestration template](img/servicedialog-from-heat.png)

1. Click on ***Save*** to create the Service Dialog

    ![service dialog from orchestration template created](img/servicedialog-from-heat-created.png)

### Verify the Service Dialog

The Service Dialog was automatically created. We want to verify it was created properly and has all the expected fields.

1. Navigate to ***Automation*** -> ***Automate*** -> ***Customization***

    ![navigate to Automation, Automate, Customization](img/navigate-to-customization.png)

1. Navigate to ***Service Dialogs*** in the accordion on the left.

    ![navigate to service dialogs](img/service-dialog-accordion-after-heat.png)

1. Click on the new Service Dialog "Wordpress HEAT Template"

1. A preview will show how the Service Dialog will look like, when it's used in a Service Catalog Item.

    ![service dialog preview](img/service-dialog-heat-preview.png)

1. The preview shows us that the Service Dialog is using a default image called "fedora-20.x86_64". We do not have such an image and want to change the Service Dialog accordingly.

1. Click on ***Configuration*** -> ***Edit this Dialog***. Navigate to the element called "Image"

    ![edit the image name](img/edit-service-dialog-heat.png)

1. Change the value of the field "Default Value"

    ***Default Value:*** rhel7.2

    ![change the image name](img/service-dialog-heat-image-name.png)

1. Commit the changes by clicking on ***Save***

    ![after saving the changes](img/service-dialog-heat-updated-preview.png)

### Build a HEAT Service Catalog

The following steps will create a service catalog.

1. The next step is to create a service catalog. First we have to navigate to ***Services*** -> ***Catalogs***.

    ![navigate to services, catalog](img/navigate-to-service-catalog.png)

1. On this screen click on ***Catalogs*** on the left

    ![service catalogs](img/service-catalogs.png)

1. Click on ***Configuration*** and ***Add a New Catalog***

1. Fill out name and description:

    ***Name:*** HEAT Templates

    ***Description:*** Deploy HEAT Templates from the Catalog

    ![add a new catalog](img/add-a-new-catalog-heat.png)

1. Click ***Add*** to save the Service Catalog

### Build a HEAT Service Catalog Item

To put everything together we create a Service Catalog Item similar to before.

1. Navigate to ***Services*** -> ***Catalogs***

    ![navigate to services, catalog](img/navigate-to-service-catalog.png)

1. Click on ***Catalog items*** in the accordion on the left.

    You should already see three Service Catalogs:

    ***Unassigned:*** Catalog Items which are not published yet, will be listed here

    ***Virtual Machines:*** the Service Catalog we created in the first part of the lab

    ***HEAT Templates:*** the Service Catalog you just created

    ![navigate to catalog items](img/navigate-to-catalog-items-heat.png)

1. In the ***Configuration*** Menu, click on ***Add a New Catalog Item***

1. Chose the Catalog Item Type. For this example we want to use HEAT on OpenStack which is an Orchestration provider, so click on ***Orchestration***

    ![select catalog item type](img/select-catalog-item-type-heat.png)

1. The next dialog will ask for the details for the new Catalog Item

    The name of the Catalog Item shown in the UI:

    ***Name:*** Wordpress

    A more descriptive text about the Catalog Item:

    ***Description:*** Wordpress from HEAT

    Check the "Display in Catalog" box. If not selected, the Catalog Item will not be visible to users. This can be used for Items which are either still in draft mode, or should only be ordered as a part of a bundle.

    ***Display in Catalog:*** check this box

    Select the previously created Service Catalog:

    ***Catalog:*** HEAT Templates

    Select the previously created Service Dialog:

    ***Dialog:*** Wordpress HEAT Template

    The template to execute:

    ***Orchestration Template:*** Wordpress HEAT Template

    Select on which provider the HEAT Template should be executed:

    ***Provider:*** OpenStack

    All other fields on this tab can remain unchanged.

    ![service catalog item details](img/service-item-details-heat.png)

    Entry Points are the hooks into CloudForms' powerful Automation Framework. It allows administrators to define provisioning, reconfiguration and retirement workflows which are different from the out of the box behavior. For example we could add integration into an IP Address Management Tool, a ticketing system or a CMDB Service. For this lab, we want to stick with the out of the box experience and leave those fields unchanged.

1. OPTIONAL: Click on the ***Details*** tab. You can provide some more descriptive explanation about the Service Catalog Item. We can even use basic HTML formatting in this box.

1. Finally click on ***Add*** to save the Service Catalog Item

    ![catalog item saved](img/catalog-item-saved-heat.png)

### Order the HEAT Wordpress Catalog Item

For sure you want to test the Catalog Item you just created!

1. Navigate to ***Services*** -> ***Catalogs*** and then click on ***Service Catalogs*** in the accordion on the left.

    ![navigate to services, catalog](img/navigate-to-service-catalog.png)

1. You should see the Service Catalog Item we just created:

    ![all services](img/all-services-heat.png)

1. Click on the Service Catalog Item to see more details.

    ![service item details](img/order-wordpress-item.png)

1. Click on ***Order***

1. Fill out the form:

    Select the tenant into which you want to deploy. There is only one tenant in OpenStack called "admin"

    ***Tenant:*** Admin

    Specify a stack name for your deployment:

    ***Stack Name:*** wordpress001

    For all other fields the provided default values can be accepted. Note that the image name is "rhel7.2" as you specified in your dialog.

    ![order HEAT template](img/order-wordpress-heat-template.png)

    Click on ***Submit*** to start the deployment.

1. You will be redirected to the request queue where you can see CloudForms working on your request.

    ***Note:*** Since we are using nested virtualization to run these labs, performs will be slow and it can take several minutes to complete the request (20-30 minutes).

    ![after ordering heat service catalog item](img/after-ordering-heat.png)

### Verify provisioning in OpenStack

Let's log into OpenStack to see what's happening there.

1. Log into OpenStack:

    [https://osp-&lt;GUID&gt;.https://osp-<GUID>.rhpds.opentlc.com](https://osp-&lt;GUID&gt;.https://osp-<GUID>.rhpds.opentlc.com)

    ***Note:*** Make sure you use the HTTPS URL!

    ***username:*** admin

    ***Password:*** r3dh4t1!

    ![dashboard after login](img/osp-after-login.png)

1. Navigate to ***Project*** in the menu bar on the top

    ![navigate to project](img/osp-navigate-to-project.png)

1. Navigate to ***Orchestration*** -> ***Stacks***

    ![navigate to orchestration stacks](img/osp-navigate-to-stacks.png)

1. You should see your stack. It might already be completed or still in progress. If you can't see it yet, wait a minute and reload the page.

    ![stack completed](img/osp-stack-completed.png)

1. Click on the stack to get the details

    ![stack details](img/osp-stack-details.png)

This concludes this section of the lab.

## CloudForms 4.5 with Ansible batteries included

This lab will guide you through the process of using the new embedded Ansible features of CloudForms 4.5.

### Introduction to Ansible

Today, every business is a digital business. Technology is your innovation engine, and delivering your applications faster helps you win. Historically, that required a lot of manual effort and complicated coordination. But today, there is Ansible - the simple, yet powerful IT automation engine that thousands of companies are using to drive complexity out of their environments and accelerate DevOps initiatives.

Red Hat CloudForms can integrate with IaaS, PaaS, public and private cloud and configuration management providers. Since version 4.2 of CloudForms, it can also integrate with Ansible Tower by Red Hat. The latest version which is 4.5, has a new "embedded Ansible" role which allows it to run Playbooks, manage credentials and retrieve Playbooks from a source control management like git.

This integration allows customers to build service catalogs from Ansible Playbooks to allow end users to easily browse, order and manage resources from Ansible. Ansible Playbooks can be used in Control Policies which can not only detect problems, but also automatically fix them.

### Make sure embedded Ansible role is enabled and running

Before we start,  we want to make sure the embedded Ansible role is enabled and running.

1. Log into your CloudForms Appliance

1. Click on your user name on the top right and click on ***Configuration***

    ![navigate to configuration](img/navigate-to-configuration.png)

1. Make sure the "Embedded Ansible" Role is enabled

    ![ansible role enabled](img/ansible-role-enabled.png)

1. Click on ***Diagnostics*** in the accordion on the left and click on the ***Workers*** tab

1. Make sure you can see a line indicating the "Embedded Ansible Worker" is in state "started"

    ![ansible worker started](img/ansible-worker-started.png)


Logoff as demouser and login back as Admin


### Add a Git repository of Ansible Playbooks

To be able to run Ansible Playbooks, they have to become available in CloudForms. Custom git repositories can be used as well as Github, Gitlab or others. Other repository types like Subversion or Mercurial are planned for later versions.

1. Navigate to Automation, Ansible, Repositories.

    ![navigate to Ansible repositories](img/navigate-to-ansible-repo.png)

1. Click on ***Configuration***, ***Add New Repository***

1. Fill in the form.

    ***Name:*** Github

    ***Description:*** Example Playbooks

    ***URL:*** [https://github.com/cbolz/rhte-fy18.git](https://github.com/cbolz/rhte-fy18.git)

    ***SCM Update Options:*** check "Update on Launch"

    ![add a new repository](img/add-ansible-repository.png)

1. Click on ***Add*** to save the settings

***Note:*** It takes a few seconds for the action to complete. A pop up notification will inform you after the task was completed.

### Add vCenter credentials

For one of the following labs, the Playbook needs to be able to log into the vCenter provider. For this to work, we need to store the necessary credentials.

1. Navigate to ***Automation*** -> ***Ansible*** -> ***Credentials***

    ![navigate to ansible credentials](img/navigate-to-ansible-credentials.png)

1. Click on ***Configuration*** -> ***Add New Credentials***

1. Provide the credentials in the form:

    ***Name:*** vCenter

    ***Credentials Type:*** VMware

    ***Username:*** root

    ***Password:*** r3dh4t1!

    ***vCenter Host:*** vcenter.example.com

    ![vcenter credentials](img/vcenter-credentials.png)

1. Click ***Add*** to save the credentials

***Note:*** It takes a few seconds for the action to complete. A pop up notification will inform you after the task was completed. You can track the progress in the Tasks section.

In the top right corner of the screen navigate to ***Administrator*** -> ***Tasks***

![tasks](img/tasks.png)

And click in ***All Other Tasks***

![All-Other-Taks](img/all-other-tasks.png)

### Verify repository sync

In the meantime the repository you created should have completed the initial synchronization. Let's check all Playbooks have been successfully imported and are available for us to use.

1. Navigate to ***Automation*** -> ***Ansible*** -> ***Playbooks***

    ![navigate to ansible Playbooks](img/navigate-to-ansible-playbooks.png)

1. You should see a list of available Playbooks

    ![list of available Playbooks](img/list-pf-playbooks.png)

If there are no Playbooks listed, check the repository was configured correctly. Click the notification icon on the top right (the little bell icon) and check if there are any errors listed. The initial import can also take a minute or two, did you wait long enough?

### Install pysphere

In order to use the Ansible VMware modules you need to install a python library call "pysphere". You need to ssh to you student workstation and jump to the CloudForms server.

`
$ sudo easy_install -U pysphere
`

### Build a Service Catalog to create and delete users

In this lab we will use an Ansible Playbook to create a local user in CloudForms. This example will also demonstrate how we can define a retirement process as well. In CloudForms' understanding of complete life cycle management, every object has a provisioning and a retirement workflow.

### Create a Service Catalog for Ansible Playbooks

1. Navigate to ***Services*** -> ***Catalogs***

    ![navigate to service catalogs](img/navigate-to-service-catalog.png)

1. Click on ***Catalogs*** in the accordion on the left

1. Click on ***Configuration*** -> ***Add a New Catalog***

    ***Name:*** Ansible

    ***Description:*** Ansible Service Catalog Items

    ![create ansible catalog](img/create-ansible-catalog.png)

1. Click ***Add*** to save the new catalog

### Create a Service Catalog Item for the Playbook

1. Click on ***Catalog Items*** in the accordion on the left

    ![navigate to service catalog items](img/add-catalog-item.png)

1. Click on ***Configuration*** -> ***Add a New Catalog Item***

1. Select ***Ansible Playbook*** as "Catalog Item Type"

    ![add catalog item ansible Playbook](img/add-catalog-item-ansible-playbook.png)

    ***Note:*** Do not select Ansible Tower! We do not use Ansible Tower in this lab, but the embedded Ansible role of CloudForms.

1. Fill out the form to define the service catalog item:

    ***Name:*** Create User

    ***Description:*** Order this catalog item to create a new user

    ***Display in Catalog:*** Yes (check the box)

    ***Catalog:*** Ansible

    ***Repository:*** Github

    ***Playbook:*** create-user.yml

    ***Machine Credentials:*** CFME Default Credentials

    In the box ***Variables & Default Values*** we can enter the variables the Playbook requires:

    ***Variable:*** create_user_name

    ***Default:*** example

    Click on the little plus icon (+) to save the variable. Repeat the process for the second variable:

    ***Variable:*** create_user_password

    ***Default:*** secret

    Click on the little plus icon (+) to save the variable.

    ***Dialog:*** create new

    ***Dialog name:*** create-user

    ![create user service dialog](img/create-new-user-prov.png)

1. Click on the tab ***Retirement*** to switch to the second page of the form.

    ***Repository:*** Github

    ***Playbook:*** delete-user.yml

    ***Machine Credentials:*** CFME Default Credentials

    There are no variables needed for retirement and the ***Variables & Default Values*** can be left empty.

    ![create user service dialog retirement](img/create-new-user-retire.png)

1. Click on ***Add*** to save the catalog item

### Order the "create user" Service Catalog Item

To make sure everything works as expected, we want to test the Catalog Item we just created.

1. Navigate to the Service Catalog by clicking on ***Services*** -> ***Catalogs***

    ![navigate to service catalog](img/navigate-to-service-catalog.png)

1. Click on ***Service Catalog*** in the accordion on the left

1. Click on the Catalog Item you just created:

    ![navigate to service catalog](img/service-catalog-overview-create-user.png)

1. Click ***Order***

1. The default values in the form can be left alone. Optionally you can specify a different user name and password

    ![create user order form](img/create-user-order-form.png)

1. Click ***Submit***

    After clicking "Submit" you will be redirected to the Request Queue.

    ![request queue after ordering create user](img/request-queue-create-user.png)

### Monitor create user Playbook execution

When executing an Ansible Playbook with the embedded role in CloudForms, a "Service" object is automatically created. This service object gives us more details about the executed Playbook. It provides the output of the Playbook and it allows us to trigger retirement.

1. Navigate to ***Services*** -> ***My Services***

    ![navigate to my services](img/navigate-to-my-services.png)

1. You should see a new tile representing the Ansible Playbook Service you just ordered

    ***Note:*** If you don't see the tile yet, wait a minute and try again.

    ![create user service tile](img/my-service-create-user-tile.png)

1. After clicking on the icon, we can see more details about the service which was created

    ![create user service details](img/create-user-service-details.png)

    Since this Service does not create a Virtual Machine, the box "VMs" will always say "No Records found"

1. Click on the ***Provisioning*** tab to see the output of the Ansible Playbook

    ![ansible Playbook output](img/ansible-playbook-output.png)

    If the Playbook execution has not completed, you can click the reload icon to refresh the information. The ***Reload*** icon is represented by a little arrow, left of the ***Configuration*** menu.

    ![reload icon](img/reload-icon.png)

    ***Note:*** If the Playbook execution has not started yet, you might not see any details in the "Provisioning" tab. Wait a minute and reload once more.

### Verify Playbook results

To make sure the user was really created, follow these steps.

1. Click on your username on the top right and click on ***Configuration***

    ![navigate to configuration](img/navigate-to-configuration.png)

1. Click on ***Access Control*** in the accordion on the left

    ![navigate to access control](img/access-control.png)

1. Click on ***Users*** and you should see the user you just created (in this screenshot the user is called "example")

    ![user example exists](img/user-example.png)

1. OPTIONALLY: If you want, you can log out of CloudForms and try to log in with the user you just created. Click on your username on the top right and ***Logout***.

    ![logout](img/logout.png)

### Build a Service Catalog to deploy Virtual Machines

In this second part of the lab we want to use an Ansible Playbook to deploy a Virtual Machine in VMware vCenter. The necessary Playbook should already be in your repository.

1. Click on ***Catalog Items*** in the accordion on the left

    ![navigate to service catalog items](img/add-catalog-item.png)

1. Click on ***Configuration*** -> ***Add a New Catalog Item***

1. Select ***Ansible Playbook*** as "Catalog Item Type"

    ![add catalog item ansible Playbook](img/add-catalog-item-ansible-playbook.png)

    ***Note:*** Do not select Ansible Tower! We do not use Ansible Tower in this lab, but the embedded Ansible role of CloudForms.

1. Fill out the form to define the Service Catalog Item:

    The name of the Service Catalog Item:

    ***Name:*** Provision Virtual Machine

    More description details about the Service Catalog Item

    ***Description:*** Order this catalog item provision a Virtual Machine on VMware vCenter

    Check this box to make the Service Catalog Item visible in the Service Catalog. This remains unselected for Service Catalog Items which are still in draft mode or should only be used as a part of a Service Catalog Bundle:

    ***Display in Catalog:*** Yes (check the box)

    The Service Catalog in which this Service Catalog Item should be listed:

    ***Catalog:*** Ansible

    The Git repository from which we want to run our Playbook:

    ***Repository:*** Github

    The name of the actual Playbook:

    ***Playbook:*** create_vm_from_template.yml

    Credentials used to run the Playbook:

    ***Machine Credentials:*** CFME Default Credentials

    If you want to run your Playbook against a Cloud Provider, you have to select which one:

    ***Cloud Type:*** VMware

    The credentials used to log into the Cloud Provider:

    ***Cloud Credentials:*** vCenter

    In the box ***Variables & Default Values*** we can enter the variables the Playbook requires. Those variables are defined in the Ansible Playbook. By specifying them here, CloudForms can populated those variables when somebody order the Service Catalog Item.

    If you want to learn more about variables in Ansible Playbooks, have a look at the [Ansible Documentation](http://docs.ansible.com/ansible/playbooks_variables.html).

    ***Variable:*** vcenter_hostname

    ***Default:*** vcenter.example.com

    Click on the little plus icon (+) to save the variable. Repeat the process for the second variable:

    ***Variable:*** esxi_host

    ***Default:*** 192.168.0.51

    Click on the little plus icon (+) to save the variable. Repeat the process for the second variable:

    ***Variable:*** datacenter

    ***Default:*** DC01

    Click on the little plus icon (+) to save the variable. Repeat the process for the second variable:

    ***Variable:*** template

    ***Default:*** rhel6tmpl

    Click on the little plus icon (+) to save the variable. Repeat the process for the second variable:

    ***Variable:*** vmname

    ***Default:*** changeme

    Click on the little plus icon (+) to save the variable.

    ***Dialog:*** create new

    ***Dialog name:*** provision-vm-vcenter

    ![create user service dialog](img/vm-from-template-prov.png)

1. Click on ***Add*** to save the Service Catalog Item. It can take a few moments for the changes to be saved.

    ![catalog item was created](img/vm-prov-catalog-item-created.png)

### Order the Virtual Machine Provisioning Service Catalog Item

Once more, we want to test the result and see everything works as expected.

1. Navigate to ***Services*** -> ***Catalogs***

    ![navigate to service catalogs](img/navigate-to-service-catalog.png)

1. Click on the Service Catalog Item we just created "Provision Virtual Machine"

    ![provision virtual machine catalog item](img/provision-vm-catalog-item.png)

1. Click ***Order***

1. If you specified the dialog elements like described before, your form should look like this and all the provided default values can be accepted.

    ![provision virtual machines details](img/provision-vm-details.png)

1. Click on ***Submit***

    After you click on "Submit" you will be redirected to the requests queue.

    ![requests queue after ordering provision VM](img/requests-queue-after-vm-prov.png)

### Monitor VM provisioning Playbook execution

When executing an Ansible Playbook with the embedded role in CloudForms, a "Service" object is automatically created. This service object gives us more details about the executed Playbook. It provides the output of the Playbook and it allows us to trigger retirement.

1. Navigate to ***Services*** -> ***My Services***

    ![navigate to my services](img/navigate-to-my-services.png)

1. You should see a new tile representing the Ansible Playbook Service you just ordered

    ***Note:*** If you don't see the tile yet, wait a minute and try again.

    ![create user service tile](img/my-service-provision-vm-tile.png)

1. After clicking on the icon, we can see more details about the service which was created

    ![create user service details](img/vm-prov-service-details.png)

    Since this Service does not create a Virtual Machine, the box "VMs" will always say "No Records found"

1. Click on the ***Provisioning*** tab to see the output of the Ansible Playbook

    ![ansible Playbook output](img/vm-prov-ansible-Playbook-output.png)

    If the Playbook execution has not completed, you can click the reload icon to refresh the information. The ***Reload*** icon is represented by a little arrow, left of the ***Configuration*** menu.

    ![reload icon](img/reload-icon.png)

### Extend CloudForms builtin Capabilities

In this lab you have so far learned how to use Ansible Playbooks to orchestrate and execute configuration actions. CloudForms is internally using a powerful and extensible framework that defines what happens "under the hood". This feature is called "Automate". "Automate" allows us to understand how things are done and even more interestingly, it allows us to add features which are not coming out of the box.

"Automate" code can either be developed directly in the User Interface, or it can be imported from a Git repository. For this lab we want to keep things simple. We will add a Git repository with a simple method to make the Service Dialog easier to use.

### Add a Git repository for Automate

"Automate" code can either be developed and written directly in the CloudForms Web UI, or it can be imported from a Git repository. We will do the latter:

1. Navigate to ***Automation*** -> ***Automate*** -> ***Import/Export***

    ![navigate to automate import/export](img/navigate-to-automate-import-export.png)

1. Use the following URL to access the Git repository:

    [https://github.com/cbolz/partner-conference-2017-labs.git](https://github.com/cbolz/partner-conference-2017-labs.git)

    ![adding the Automate Git repository](img/adding-automate-git.png)

1. Click ***Submit***. It will take a few moments to check the Git repository.

1. The "Branch/Tag" and "Branch" fields allow us to import different tags or branches, for example "Development", "Testing", "QA", etc.

    For this lab, we stick with the defaults and click on ***Submit***

    ![select Automate tag or branch](img/select-automate-tag-branch.png)

1. The first import can take a few moments. After that you should see the following confirmation:

    ![after first Automate import](img/after-first-automate-import.png)

### Verify Automate import

We want to make sure the Automate Code was properly imported.

1. Navigate to ***Automation*** -> ***Automate*** -> ***Explorer***

    ![navigate to Automate Explorer](img/navigate-to-automate-explorer.png)

1. "Automate" code is organized in "Datastores". Two Datastores are shipped with CloudForms:

    * ManageIQ: These methods are a verbatim copy of the Open Source Community version
    * RedHat: These methods are only shipped with Red Hat CloudForms and are supported by Red Hat

    You can now see an additional third Datastore called "PConf17", which is the one you just imported. Users can create as many additional datastores as they want, but they can not modify or delete the two datastores shipped with the product. Datastores are stacked and prioritized which allows separation of out of the box functionality from custom code.

    The screenshot was created after expanding all folders (which are actually called "Namespaces" and "Classes":

    ![Automate with custom method](img/automate-with-custom-method.png)

This concludes the preparation for the next part of the lab.

### Optimize the Dialog

The Service Dialog we created so far, is not ideal for most use cases. We want users to focus on getting their service as quickly and easily as possible. An ideal Service Dialog only asks the absolutely necessary questions. With this in mind, we can optimize the automatically created Service Dialog created in the previous part of the lab.

1. Navigate to ***Automation*** -> ***Automate*** -> ***Customization***

    ![navigate to customization](img/navigate-to-customization.png)

1. Click on ***Service Dialog*** in the accordion on the left

    ![navigate to service dialogs](img/service-dialog-accordion.png)

1. Click on the Dialog which was created in the previous step "provision-vm-vcenter"

1. Click on ***Configuration*** -> ***Copy this Dialog***. We want to keep the original version of the Dialog, which will allow us to have a backup.

1. Edit the Label and Description to something a bit more meaningful

    ***Label:*** provision-vm-vcenter-v2

    ***Description:*** Optimized version of the Service Dialog

    ***Note:*** Do not click on ***Add*** yet, we want to do some more changes!

1. We want to do several changes on this Dialog.

    Change the Label to something more meaningful:

    ***Label:*** provision-vm-vcenter-v2

1. The elements in the "Options" box will always be left to the default values for our Service Catalog Item to work. Since our users are never going to change any of the field in the "Options" box, we can simply delete the entire box.

    Click on the Box "Options" and then on the little trash bin icon to delete it and all its child elements.

    ![delete options box](img/delete-options-box.png)

    ***Note:*** Make sure you have highlighted the correct element! If you deleted the wrong element by accident, you can click on ***Cancel*** and start over.

1. The ESXi host which will actually create the virtual machine, is always the same in this lab. We can hide the element to simplify the Dialog further.

    Click on the Element "esxi_host" and unselect the "visible" box

    ![make host invisible](img/esxi-visibility.png)

1. The same applies for the "Datacenter". In this lab, there is only one.

    ![make datacenter invisible](img/datacenter-visibility.png)

1. To finish the our optimizations, we want to make the vCenter a dynamic drop down. Instead of providing possible values as a hard coded list, or asking the user for manual input, we can use program code to create a list of applicable options.

    In this example, we want the list of available vCenters dynamically populated (Although there is still only one vCenter and the value is questionable at best. But it's a good example of CloudForms' capabilities nonetheless)

    Click on the Element "vcenter_hostname" and change the type to "Drop down list". Then click the check box "Dynamic". This will change the form and show us new fields:

    ![form after selecting dynamic](img/vcenter-dynamic-checked.png)

    Click on "Entry Point". A window will pop up which allows us to specify which method instance should be called to populate this Element.

    Select the Instance called "get_vcenter_list" and click ***Apply***.

    ![select get_vcenter_list instance](img/get_vcenter_list-instance.png)

    The resulting Service Dialog Element should look like this:

    ![vcenter dynamic drop down list](img/vcenter-dynamic-drop-down.png)

1. Click on ***Add** to save all changes

### Update the Service Catalog Item

We have to change the Service Catalog Item to use the Service Dialog we just created.

1. Navigate to ***Services*** -> ***Catalogs***

    ![navigate to service catalogs](img/navigate-to-service-catalog.png)

1. Navigate to ***Catalog Items*** in the accordion on the left and click on the "Provision Virtual Machine" Service Catalog Item

    ![navigate to catalog items](img/vm-prov-service-catalog-item.png)

1. Click on ***Configuration*** -> ***Edit this Item***

1. In the ***Dialog*** Section of the UI, change the value from "provision-vm-vcenter" to "provision-vm-vcenter-v2"

    ![change dialog to provision-vm-vcenter-v2](img/dialog-vm-provision-vcenter-v2.png)

1. Click ***Save*** to commit the changes

### Test the new Service Dialog

We want to see how the resulting Service Catalog Item looks like.

1. Navigate to ***Services*** -> ***Catalogs***

    ![navigate to service catalogs](img/navigate-to-service-catalog.png)

1. Make sure you are on the "Service Catalogs" tab in the accordion on the left

1. Order the "Provision Virtual Machine" Service Catalog Item

    ![provision virtual machine](img/provision-vm-catalog-item.png)

1. Note the Service Dialog has changed compared to before. You should notice a few fields are gone and the vCenter is now a drop down list. "vCenter" should already be selected for you.

    ![new provision virtual machine dialog](img/order-new-virtual-machine-dialog.png)

1. If you want, you can go ahead and submit the order

## Policies and Ansible

In this lab we will cover how to create an action in CoudForms that executes an Ansible Playbook. 

### Creating the Service

Control Policies drive Control Actions. Ansible Playbooks can now be executed as a control action, this is done by the control action calling a service. Therefore we need to create a service for the action to call.

First we need to create a Catalog to store the service in, do this by clicking Services/Catalogs and create new by clicking Configuration button and selecting Add New Catalog.

### Create a Service Catalog Item for the Playbook

1. Click on ***Catalog Items*** in the accordion on the left

    ![navigate to service catalog items](img/add-catalog-item.png)

1. Click on ***Configuration*** -> ***Add a New Catalog Item***

1. Select ***Ansible Playbook*** as "Catalog Item Type"

    ![add catalog item ansible Playbook](img/add-catalog-item-ansible-playbook.png)

    ***Note:*** Do not select Ansible Tower! We do not use Ansible Tower in this lab, but the embedded Ansible role of CloudForms.

1. Fill out the form to define the service catalog item:

    ***Name:*** VM reset for CPU and Memory

    ***Description:*** Reconfigure VMware VM for CPU and Memory

    ***Display in Catalog:*** No (uncheck the box)

    ***Catalog:*** Ansible

    ***Repository:*** Github

    ***Playbook:*** vmware_reconfigure_vm.yml

    ***Machine Credentials:*** CFME Default Credentials

    ***Cloud Type*** VMware

    ***Cloud Credential*** vCenter

    In the box ***Variables & Default Values*** we can enter the variables the Playbook requires:

    ***Variable:*** vcenter_server

    ***Default:*** vcenter.example.com

    Click on the little plus icon (+) to save the variable. Repeat the process for the second variable:

    ***Variable:*** guest_server

    ***Default:*** \<TBD>

    Click on the little plus icon (+) to save the variable.

    ***Dialog:*** create new

    ***Dialog name:*** vm_reconfig

    ![vm-reconfig-service](img/vm-reconfig-service.png)

### Creating Control Action

1. Navigate to ***Control*** -> ***Explorer*** and click on the ***Actions*** accordion

    ![control-explorer](img/control-explorer.png)

1. Click on the ***Actions*** accordion

    ![actions](img/actions.png)

1. Select Configuration/Add a new Action

    ![add-new-action](img/add-new-action.png)

1. Fill out the form as follows

    ***Description:*** Reset VM for CPU and Memory

    ***Action Type:*** Run Ansible Playbook

    ***Playbook Catalog Item:*** VM reset for Memory and CPU

    ***Inventory:*** Localhost

    Leave the inventory on “Localhost” this is because the playbook that is run as part of the service you created is to be ran on the CloudForms appliance. The other options are

    - Run the playbook in the service on the machine that raises the event.
    - Comma Delimited list of Hosts.

    ![create-action-form](img/create-action-form.png)

1. Click Add

    Next we will create the Policy to call the action. The use case that will be demonstrated is when a VM changes its hardware settings, CloudForms will change it back.

### Create VM Control Policy

1. Navigate to ***Policies** and then select ***VM Control Policies***

    ![control-policies](img/control-policies.png)

1. Select Configuration/Add a New VM and Instance Control policy

    ![add-new-control-policy](img/add-new-control-policy.png)

1. In the form you just need to provide the ***Description***

    ***Description:*** Reset VM for CPU and Memory

    ![add-new-control-policy-form](img/add-new-control-policy-form.png)

### Setting Event Assignment

1. Once added click Configuration/Edit this Events Assignment

    ![edit-event-asignments](img/edit-event-asignments.png)

1. Scroll down and select “VM Settings Change” under the VM Configuration

    ![vm-settings-change](img/vm-settings-change.png)

1. Click Save

### Setting Control Action on Event

1. Click on the Event that is now save to the policy

    ![event](img/event.png)

1. Select Configuration/Edit Actions for the Policy Event

    ![edit-actions](img/edit-actions.png)

1. Scroll the Available Actions For Conditions that are TRUE and move the Action you just created to the Selected Actions

    ![actions-for-conditions](img/actions-for-conditions.png)

1. Click Save

    The policy will react to events that are “VM Settings Change”, upon the event detected it will run the action “Reconfigure VMware VM for CPU and Memory” that is in turn a Service that is a Ansible Playbook.

### Creating and Assigning Policy Profile

For a policy to work, it needs a policy profile to be attached to. The policy profile also needs to be assigned to an object in CloudForms.

1. Navigate to ***Control*** -> ***Explorer*** -> ***Policy Profiles***

    ![navigate-policy-profiles](img/navigate-policy-profiles.png)

1. Click Configuration/Add New Policy Profile

    ![add-new-policy-profile](img/add-new-policy-profile.png)

1. Provide a ***Description***

    ***Description:*** Desired State Policies

1. Move the “Reset VM for CPU and Memory” policy from available to Profile Policies list.

    ![move-policy](img/move-policy.png)

1. Click Save

### Assign the policy profile

1. Navigate to ***Compute*** -> ***Infrastructure*** -> ***Virtual Machines***

    ![navigate-compute-infrastructure-vms](img/navigate-compute-infrastructure-vms.png)

1. Select a Power Off VM

1. Go to ***Policy*** -> ***Manage Policies***

    ![assign-policy-vm](img/assign-policy-vm.png)

1. Select the “Desired State Policy Profile”

    ![assign-policy-vm2](img/assign-policy-vm2.png)

1. Click Save

    This has assigned the Desired State Policy Profile to the individual VM. When the VM is configured for CPU or Memory, CloudForms will reset it back to 1CPU and 1GB memory.

### Testing the Policy Profile

We will see the output in CloudForms in the form of a service in my services as well as the actual VM inventory will change. To see more real time, it's advised during testing to open the policy.log file on the CloudForms appliance. This shows when events are caught by CloudForms and confirms the policy matches. 

Start by going to vSphere Web Client and selecting the VM that you identified for your service and policy earlier.

1. Go to the vCenter console, pick the VM you assigned the Policy and modify the CPU and Memory values to 

    ***CPU:*** 3

    ***Memory:*** 4096 MB

    ![vmware-edit-settings](img/vmware-edit-settings.png)

    You can see the vSphere Web Client task running to change the CPU and Memory.

1. Go back to the CloudForms console and navigate to ***Services*** -> ***Requests***

    ![navigate-to-services-requests](img/navigate-to-services-requests.png)

1. Wait until your request (service) is finished

    ![policy-service](img/policy-service.png)

1. Go back to the vCenter console and verify that is has 1 CPU and 1 GB of RAM

    ![verify-vmware-vm](img/verify-vmware-vm.png)

## Advanced labs

If you were able to complete all the steps and still have some time left, here are a couple of things you can do to get more familiar with CloudForms.

### Use the Self Service user Interface

The user interface we used so far is often referenced as the "Operations UI" or the "Classic UI". A new, more modern, Self Service user Interface is also available and receives improvements with every release.

The Self Service user Interface can be accessed by appending the string "self_service" to the Appliance URL.

[https://cf-&lt;GUID&gt;.labs.rhepds.com/self_service](https://cf-&lt;GUID&gt;.labs.rhepds.com/self_service)

You can login with the same credentials as before.

### Use role Based Access Control to publish Service Catalog

So far we have created Catalog Items which are visible to any logged in user. In most Enterprise environments, specific Service Catalog items should only be accessible for certain user groups.

CloudForms offers a very granular system for role Based Access Control (RBAC). This allows system administrator to grant or deny specific privileges to reduce visibility, reduce risk of human errors or provide better cost control.

In this advanced lab we want only specific Catalog Items to be available for certain user groups. CloudForms is using tags to identify objects. For example, if a Service Catalog Item is tagged as "Department Engineering" only users which are in a group which is also tagged as "Department Engineering" will see and be able to order this Catalog Item.

### User Groups

A user is always member of at least one user group. The group defines the visibility granted to all member users. For example, members of the group "Department Engineering" can see all objects tagged with this tag.

### Roles

The role defines which actions are allowed to groups associated to this role. For example the role can grant the privilege to start or stop Virtual Machines, manage Service Catalog items, or define and use reports.

Since roles can be associated to multiple groups, they can be reused. A user in Department Engineering might have the same privileges as a user in Department Sales, but they will see different objects which they can interact with.

### More details

If you want to learn more about CloudForms' Role Based Access Control, you can read the [official product documentation](https://access.redhat.com/documentation/en/red-hat-cloudforms/). The chapter [access control](https://access.redhat.com/documentation/en-us/red_hat_cloudforms/4.5/html/general_configuration/configuration#access-control) in the [General Configuration](https://access.redhat.com/documentation/en-us/red_hat_cloudforms/4.5/html/general_configuration/) Guide also provides more background information. Last but not least, there is a good summary about [Using Tags for Access Control](http://cloudformsblog.redhat.com/2016/10/13/using-tags-for-access-control/) on the [official CloudForms Blog](http://cloudformsblog.redhat.com).

### Create a Role

For this lab, we first want to create a role which we want to use for testing.

1. Navigate to ***Configuration*** on the top right menu

    ![navigate to configuration](img/navigate-to-configuration.png)

1. Click on ***Access Control*** in the accordion on the left

    ![access control](img/navigate-to-access-control.png)

1. Click on ***roles*** and ***Configuration*** -> ***Add a new role***

    ![add a new role](img/add-a-new-role.png)

1. We want to define a new role, which has enough privileges to order and interact with Service Catalog Items.

    ***Name:*** Self Server role

    ***Access Restriction for Services, VMs, and Templates:*** None

    Defining the privileges is actually very simple. The tree view allows us to simply select or unselect the privileges we want to grant to users associated to this role.

    1. Let's unselect all items on the first level, except for "Services".

    1. Click on the little triangular icon next to "Services" to open the sub folder. Make sure "My Services", "Workloads" and "Request" are selected.

    1. Click on the little triangular icon next to "Catalogs Explorer" and make sure everything except "Service Catalogs" is not selected.

    The resulting dialog should look like this:

    ![defined self server role](img/define-self-service-role.png)

1. Click ***Add*** to save the new role

1. Now we want to create a group associated to this role. Click on ***groups*** and ***Configuration*** -> ***Add a new group***

    ![add a new group](img/add-new-group.png)

### Create a new Group

Next we want to create a group and assign it to the role we just created.

1. Create the new group

    ***Description:*** Self Service Engineering

    Select the role "Self Service role" you just created:

    ***role:*** Self Service role

    CloudForms also supports multiple tenants. Since we have not defined any tenants, choose the parent "My Company" tenant:

    ***Project/Tenant:*** My Company

    In "My Company Tags" click on the little triangular icon next to "Department" and click on "Engineering"

    ***Note:*** It is important to only select this particular tag and do not click on any other additional tags!

    ![define new group](img/define-new-group.png)

1. Click on ***Add*** to create this new group

### Create a new User

Finally we want to create a user which is a member of the group we just created.

1. Click on ***users*** and ***Configuration*** -> ***Add a new user***

    ![add a new user](img/add-new-user.png)

1. Create a new user with these parameters:

    ***Full Name:*** Joe Doe

    ***username:*** joe

    ***Password:*** r3dh4t1!

    ***Confirm Password:*** r3dh4t1!

    ***E-mail Address:*** joe@example.com

    ***Note:*** CloudForms is not configured to send out emails, but the email address is a mandatory field

    ***group:*** Self Service Engineering

    ![add new user Joe Doe](img/add-user-joe-doe.png)

    Click on ***Add*** to create the user

### Test user Joe Doe

So far we have not assigned any objects to the new group, but we have granted very specific rights to members of that group.

Let's see what happens if we log into CloudForms as "Joe Doe".

***Note:*** You can not log into CloudForms with different users while you're in the same browser session. You have to log out and log in again. As an alternative, you can use a different browser, if available, or you can open an additional window in "private" mode.

1. Log out of CloudForms by clicking on the user name on the top right and click on ***Logout***

    ![logout](img/logout.png)

1. Log in as user Joe Doe:

    ***username:*** joe

    ***Password:*** r3dh4t1!

    ![login as Joe Doe](img/login-as-joe-doe.png)

1. You should notice that most of the menus are gone now. On the top level menu on the left, we can only click on ***Services*** and have only four sub menus available.

1. Navigate to the service catalog

    ![navigate to service catalog](img/navigate-to-service-catalog-joe-doe.png)

1. You should notice that there are no Catalog Items available! Although we have defined some Catalog Items earlier in this lab, none of them are available to the "Self Service Engineering" group.

1. Let's logout again

    ![logout](img/logout.png)

### Grant access to certain Catalog Items

We want to make one Catalog Item available to all users which are members of the "Self Service Engineering" group.

1. Log into CloudForms as admin

1. Navigate to ***Services*** -> ***Catalogs***

    ![navigate to services catalogs](img/navigate-to-service-catalog.png)

1. Click on ***Catalog Items*** in the accordion on the left

    ![navigate to catalog items](img/navigate-to-catalog-items-heat.png)

1. Click on ***Virtual Machines*** and ***Simple VM***

    ![catalog item simple vm details](img/catalog-item-simple-vm-details.png)

1. Click on ***Policy*** -> ***Edit Tags***

    ![catalog item edit tags](img/catalog-item-edit-tags.png)

1. Assign the Tag "Department" / "Engineering" to the Catalog Item

    ![assign department engineering tag](img/assign-department-engineering-tag.png)

1. Click ***Save*** to commit the changes

### Test once more as Joe Doe

We want to do another test and see if the user Joe Doe can now see and other the Catalog Item.

1. Log out

    ![logout](img/logout.png)

1. Log in as Joe Doe

    ![login as Joe Doe](img/login-as-joe-doe.png)

1. Navigate to ***Services*** -> ***Catalogs***

    ![navigate to service catalogs](img/navigate-to-service-catalog.png)

1. Now you should see one Service Catalog Item: "Simple VM" - but no other Service Catalog Items.

    ![service catalog](img/service-catalog-joe-doe.png)

1. If you want, you can order the Service Catalog Item and should see that it will be deployed perfectly.

## Even more?

If you're already done and still have some time left, here are some ideas for advanced labs:

- try to retire the "create user" service catalog item and see if the user is indeed deleted
- try to add other Playbooks, some examples can be found on the [Official Red Hat CloudForms Blog](http://cloudformsblog.redhat.com/2017/05/31/ansible-automation-inside-cloudforms/)
- retire the virtual machine Service you ordered earlier, check what happens during retirement with the virtual machine (Is it shutdown? Deleted? Is there still a representation in the CloudForms Web UI?)
- make the second Catalog Item available for Joe Doe as well
- improve the Service Dialog and make the VM Name a mandatory field (right now, it's optional and can be left empty)
- grant Joe Doe more privileges (for example, it would be nice if he could start and stop his virtual machines)
- upload items to make the Service Catalog more appealing
- use the new Self Service user Interface by trying the "/self_service" URL on your Appliance
