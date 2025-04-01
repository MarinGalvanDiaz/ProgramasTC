% Cargar solo la cantidad de unos (y)
y = load('D:\ProgramaGenaro\resultadogood.txt');

% Graficar los datos sin eje x definido
figure;
plot(y, '.', 'Color', 'b', 'MarkerSize', 5);
xlabel('Índice de dato');
ylabel('Cantidad de unos');
title('Cantidad de unos en cadenas binarias');
grid on;