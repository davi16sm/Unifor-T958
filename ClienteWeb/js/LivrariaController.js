app.controller('LivrariaController', function ($scope, $http) {

    $scope.livro = {};
    $scope.listaLivros = [];

    $scope.adiciona = function () {
        $scope.livro.id = $scope.listaLivros.lenght+1;

        $http.post('http://localhost:3000/livros', $scope.livro).success(
            function (dados) {
                $scope.listaLivros.push($scope.livro);
                $scope.livro = {};
            }
        );
    };


    $scope.lista = function () {

        $http.get('http://localhost:3000/livros').success(
            function (dados) {
                $scope.listaLivros = dados;
            }
        );
    };

    $scope.lista();

});