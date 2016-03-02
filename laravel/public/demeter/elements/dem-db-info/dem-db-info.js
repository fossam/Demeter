Polymer({
	is:"dem-db-info",
	behaviors:[Polymer.NeonSharedElementAnimatableBehavior],
	properties:{
		database:{ observer:"receivedDatabaseInfo" },
		animationConfig: {
      		value: function() {
        		return {
        			'entry':[
	                {
	                	name:'fade-in-animation',
	                	node:this
	                },
	                {
	                	name:'hero-animation',
          				id:'hero',
          				toPage:this
		            }],
          			'exit':[
          			{
          				name:'hero-animation',
          				id:'hero',
          				fromPage:this
          			},
	                {
	                  name:'fade-out-animation',
	                  node:this
	                }]
        		}
      		}
    	}
	},
	receivedDatabaseInfo:function(){
		if(this.database.USERS.length == 0) {
			this.push("database.USERS","No Users");
		}
	},
	goToEdit:function() {
		this.fire("goToPage", 4); //opens the edit database page.
	},
	goToList:function(){
		this.fire("goToPage", 1);	//go back to database list
	},
	showAddDialog:function(){
		this.$.addUserDialog.opened = true;
	}
});