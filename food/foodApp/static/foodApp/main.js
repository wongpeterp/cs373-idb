var app = angular.module('myApp', [],function($locationProvider) {
	$locationProvider.html5Mode(true);
});

app.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
});

app.controller('RecipeController', function($scope, $http, $location) {
	$scope.recipe = $location.search()["r"];

	$http.get('/static/foodApp/RecipeData.json').then(function(res) {
		$scope.recipes = res.data;
	});
});

app.controller('CuisineController', function($scope, $http, $location) {
	$scope.cuisine = $location.search()["c"];

	$http.get('/static/foodApp/Cusines_data.json').then(function(res) {
		$scope.cuisines = res.data;
	});
});

app.controller('IngredientController', function($scope, $http, $location) {
	$scope.ingredient = $location.search()["i"];

	$http.get('/static/foodApp/IngredientsData.json').then(function(res) {
		$scope.ingredients = res.data;
	});
});



