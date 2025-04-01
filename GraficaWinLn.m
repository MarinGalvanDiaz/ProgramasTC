% Cargar solo la cantidad de unos (y)
y = load('D:\ProgramaGenaro\resultadogood.txt');

% Aplicar logaritmo natural
y_ln = log(y);

% Graficar los datos con ln(y)
figure;
plot(y_ln, '.', 'Color', 'b', 'MarkerSize', 5);
xlabel('Índice de dato');
ylabel('ln(Cantidad de unos)');
title('Cantidad de unos en cadenas binarias (Escala logarítmica)');
grid on;