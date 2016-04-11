# Demeter
Database as a Service
This is not yet an active project

##Middleware to Backend Communication
####Redis Channel: demeter

#####format:
```
[
	'command' => 'createInstance', 
	'vm' => [Id of the VM],
	'instanceId' => [Id of the instance],
	'instanceName' => [Name of the instance],
	'type' => [Instance type (mysql, mongo, oracle)], 
	'maxSize' => [Maximum size of instance],
	'username' => [Instance user username],
	'password' => [Instance user password],
	'netId' => [NetId of logged in user],
]

[
	'command' => 'updateInstance', 
	'instanceId' => [Id of the instance],
	'vm' => [Id of the VM],
	'oldInstanceName' => [Previous name of instance],
	'instanceName' => [Name of the instance],
	'maxSize' => [Maximum size of instance],
	'netId' => [NetId of logged in user],
]	

[
	'command' => 'deleteInstance', 
	'instanceId' => [Id of the instance],
	'vm' => [Id of the VM],
	'instanceName' => [Name of the instance],
	'netId' => [NetId of logged in user],
]

[
	'command' => 'backupInstance', 
	'instanceId' => [Id of the instance],
	'vm' => [Id of the VM],
	'type' => [Instance type (mysql, mongo, oracle)],
	'netId' => [NetId of logged in user],
]

 
[
	'command' => 'createInstanceUser', 
	'vm' => [Id of the VM],
	'instanceId' => [Id of the instance],
	'instanceName' => [Name of the instance],
	'username' => [Instance user username],
	'password' => [Instance user password],
	'netId' => [NetId of logged in user],
]

[
	'command' => 'resetPassword', 
	'vm' => [Id of the VM],
	'instanceId' => [Id of the instance],
	'instanceName' => [Name of the instance],
	'username' => [Instance user username],
	'password' => [Instance user password],
	'netId' => [NetId of logged in user],
]

[
	'command' => 'deleteInstanceUser', 
	'vm' => [Id of the VM],
	'instanceId' => [Id of the instance],
	'instanceName' => [Name of the instance],
	'username' => [Instance user username],
	'netId' => [NetId of logged in user],
]


[	'command' => 'init', 
	'vm' => [Id of the VM],
	'type' => [VM type (mysql, mongo, oracle)],
	'netId' => [NetId of logged in user],
]

[
	'command' => 'updateVm', 
	'vm' => [Id of the VM],
	'type' => [VM type (mysql, mongo, oracle)],
	'netId' => [NetId of logged in user],
]

[
	'command' =>  'deleteVm', 
	'vm' => [Id of the VM],
	'netId' => [NetId of logged in user],
]
```

##File Structure
This will give a quick explanation of where you can find files for this project.

####Middleware Files
Controllers: .\laravel\app\Http\Controllers

Routing (When a certain controller will be called): .\laravel\app\Http

Polymer Web Page Files: .\laravel\public\demeter

--This has a "bower_components" folder that is simply google made elements. Custom demeter elements are stored in the "elements" folder
