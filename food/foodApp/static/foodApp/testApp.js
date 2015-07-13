var app = angular.module('testApp', [],function($locationProvider) {
	$locationProvider.html5Mode(true);
});

app.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
});

/*
function MainController($scope, $location) {
	var pId = $location.absUrl();
	console.log(pId);
	$scope.test = pId;
	$scope.othertest = "working";
}
*/

app.controller("TestController", function($scope, $location) {
	$scope.url = $location.absUrl();
	$scope.ohboy = $location.search();
	$scope.recipe = $location.search()["r"];
	$scope.hello = "functioning";
	$scope.fj = {"auntruthiespotroast" : "you did it!!"};
});

/*
app.controller("TestController", function($scope) {

	$scope.test = "hello";

});

app.controller("LocationController", function($scope, $location) {
	$scope.$location = {};
	angular.forEach("protocol host port path search hash".split(" "), function(method){
		$scope.$location[method] = function(){
			var result = $location[method].call($location);
			return angular.isObject(result) ? angular.toJson(result) : result;
		};
	});

	$scope.test = "working";
});
*/