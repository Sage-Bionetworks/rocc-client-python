# User

A user of the API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the user | [optional] [readonly] 
**username** | **str** | The username of the user | 
**password** | **str** | The password of the user | [optional] 
**first_name** | **str** | The first name of the user | [optional] 
**last_name** | **str** | The last name of the user | [optional] 
**email** | **str** | An email address | 
**role** | **str** | The role of the user | [optional] [default to 'user']
**organizations** | [**list[Organization]**](Organization.md) | The organizations the user belongs to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


