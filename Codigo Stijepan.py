import json
import matplotlib.pyplot as plt
import prices as prices
import requests
import numpy as np

# CONEXIÓN A API

class BybitAPI:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://api.bybit.com"
        self.headers = {"Content-Type": "application/json"}

    def auth(self):
        timestamp = str(int(time.time() * 1000))
        message = timestamp + 'GET' + '/user/wallet'
        signature = hmac.new(bytes(self.api_secret, 'latin-1'), msg=bytes(message, 'latin-1'),
                             digestmod=hashlib.sha256).hexdigest()
        self.headers.update({"api-key": self.api_key, "api-signature": signature, "api-nonce": timestamp})

    def check_account_status(self):
        try:
            self.auth()
            url = self.base_url + "/user/wallet"
            response = requests.get(url, headers=self.headers)
            if response.status_code != 200:
                raise Exception("Error de autenticación: credenciales de API incorrectas o no válidas")
            data = json.loads(response.text)
            return data
        except requests.exceptions.RequestException as e:
            raise Exception("Error de conexión: " + str(e))
        except json.decoder.JSONDecodeError as e:
            raise Exception("Error de formato de respta")

    def place_order(self, symbol, side, qty, price):
        try:
            self.auth()
            url = self.base_url + "/order"
            payload = {"symbol": symbol, "side": side, "qty": qty, "price": price}
            response = requests.post(url, json=payload, headers=self.headers)
            if response.status_code != 200:
                raise Exception("Error de autenticación: credenciales de API incorrectas o no válidas")
            data = json.loads(response.text)
            return data
        except requests.exceptions.RequestException as e:
            raise Exception("Error de conexión: " + str(e))
        except json.decoder.JSONDecodeError as e:
            raise Exception("Error de formato de respuesta: " + str(e))
        except requests.exceptions.Timeout as e:
            raise Exception("Error de tiempo de espera: " + str(e))
        except requests.exceptions.TooManyRedirects as e:
            raise Exception("Error de límite de velocidad: " + str(e))

        def validate_side(self, side):
            if side not in ["Buy", "Sell"]:
                return False
            return True

    def check_order_status(self, order_id):
        try:
            self.auth()
            url = self.base_url + "/order?order_id=" + str(order_id)
            response = requests.get(url, headers=self.headers)
            if response.status_code != 200:
                raise Exception("Error de autenticación: credenciales de API incorrectas o no válidas")
            data = json.loads(response.text)
            return data
        except requests.exceptions.RequestException as e:
            raise Exception("Error de conexión: " + str(e))
        except json.decoder.JSONDecodeError as e:
            raise Exception("Error de formato de respuesta: " + str(e))
        except requests.exceptions.Timeout as e:
            raise Exception("Error de tiempo de espera: " + str(e))
        except requests.exceptions.TooManyRedirects as e:
            raise Exception("Error de límite de velocidad: " + str(e))

    def cancel_order(self, order_id):
        try:
            self.auth()
            url = self.base_url + "/order/cancel"
            payload = {"order_id": order_id}
            response = requests.post(url, json=payload, headers=self.headers)
            if response.status_code != 200:
                raise Exception("Error de autenticación: credenciales de API incorrectas o no válidas")
            data = json.loads(response.text)
            return data
        except requests.exceptions.RequestException as e:
            raise Exception("Error de conexión: " + str(e))
        except json.decoder.JSONDecodeError as e:
            raise Exception("Error de formato de respuesta: " + str(e))

    except requests.exceptions.Timeout as e:
    raise Exception("Error de tiempo de espera: " + str(e))

except requests.exceptions.TooManyRedirects as e:
raise Exception("Error de límite de velocidad: " + str(e))

def close_position(self, symbol, side, qty):
    try:
        self.auth()
        # Construir la URL para la solicitud de cierre de posición
        url = self.base_url + "/position/close"
        # Crear el cuerpo de la solicitud con los parámetros necesarios
        payload = {"symbol": symbol, "side": side, "qty": qty}
        # Realizar la solicitud POST
        response = requests.post(url, json=payload, headers=self.headers)
        # Verificar si el código de estado es 200
        if response.status_code != 200:
            raise Exception("Error de autenticación: credenciales de API incorrectas o no válidas")
        # Cargar la respuesta como un diccionario de Python
        data = json.loads(response.text)
        return data
    except requests.exceptions.RequestException as e:
        raise Exception("Error de conexión: " + str(e))
    except json.decoder.JSONDecodeError as e:
        raise Exception("Error de formato de respuesta: " + str(e))

def get_transaction_history(self):
    try:
        self.auth()
        # Construir la URL para la solicitud de historial de transacciones
        url = self.base_url + "/user/wallet/transactions"
        # Realizar la solicitud GET
        response = requests.get(url, headers=self.headers)
        # Verificar si el código de estado es 200
        if response.status_code != 200:
            raise Exception("Error de autenticación: credenciales de API incorrectas o no válidas")
        # Cargar la respuesta como un diccionario de Python
        data = json.loads(response.text)
        return data
    except requests.exceptions.RequestException as e:
        raise Exception("Error de conexión: " + str(e))
    except json.decoder.JSONDecodeError as e:
        raise Exception("Error de formato de respuesta: " + str(e))


def handle_rate_limit(self):
    """
    Método para manejar los límites de velocidad y capacidad de la API.
    Puede incluir funciones para esperar antes de volver a enviar una solicitud,
    o para dividir una solicitud en varias para cumplir con los límites de la API.
    """
    pass

# Variables para almacenar los valores de RSI y los parámetros de operación
rsi = 0
balance = 100
stop_loss = 0.1
take_profit = 0.3


# Función para calcular el RSI
def calc_rsi():
    global rsi
    # Cálculo del RSI utilizando la información del activo
    rsi = ...


# Función para calcular los niveles de fibonacci
def calc_fibonacci():
    # Cálculo de los niveles de fibonacci utilizando la información del activo
    fibonacci_levels = ...
    return fibonacci_levels


# Función para calcular las bandas de bollinger
def calc_bollinger():
    # Cálculo de las bandas de bollinger utilizando la información del activo
    bollinger_bands = ...
    return bollinger_bands

# estrategia de cruce de medias móviles utilizando el indicador RSI, el volumen y las bandas de bollinger

import numpy as np


# Calcular las medias móviles
def moving_average(prices, period):
    return np.mean(prices[-period:])


# Calcular el RSI
def rsi(prices, period):
    delta = prices[-1] - prices[-2]
    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)
    avg_gain = np.mean(gain[-period:])
    avg_loss = np.mean(loss[-period:])
    rs = avg_gain / avg_loss
    return 100 - 100 / (1 + rs)


# Calcular las bandas de Bollinger
def bollinger_bands(prices, period):
    sma = moving_average(prices, period)
    std = np.std(prices[-period:])
    upper_band = sma + 2 * std
    lower_band = sma - 2 * std
    return upper_band, lower_band


# Bucle para simular el trading
for i in range(1, len(prices)):
    # Calcular las medias móviles, el RSI y las bandas de Bollinger
    short_sma = moving_average(prices, short_period)
    long_sma = moving_average(prices, long_period)
    rsi_value = rsi(prices, rsi_period)
    upper_band, lower_band = bollinger_bands(prices, bollinger_period)

    # Señales de compra o venta generadas por la estrategia
    buy_signal = short_sma > long_sma and rsi_value < 30 and prices[i] < lower_band and volume[i] > average_volume
    sell_signal = short_sma < long_sma and rsi_value > 70 and prices[i] > upper_band

# estrategia de divergencia (RSI, volumen, y bandas de bolinger)


    # Calcular el RSI
    def rsi(prices, period):
        delta = prices[-1] - prices[-2]
        gain = np.where(delta > 0, delta, 0)
        loss = np.where(delta < 0, -delta, 0)
        avg_gain = np.mean(gain[-period:])
        avg_loss = np.mean(loss[-period:])
        rs = avg_gain / avg_loss
        return 100 - 100 / (1 + rs)


    # Calcular las bandas de Bollinger
    def bollinger_bands(prices, period):
        sma = np.mean(prices[-period:])
        std = np.std(prices[-period:])
        upper_band = sma + 2 * std
        lower_band = sma - 2 * std
        return upper_band, lower_band


    # Bucle para simular el trading
    for i in range(1, len(prices)):
        # Calcular el RSI y las bandas de Bollinger
        rsi_value = rsi(prices, rsi_period)
        upper_band, lower_band = bollinger_bands(prices, bollinger_period)

        # Señales de compra o venta generadas por la estrategia
        buy_signal = (prices[i] > prices[i - 1] and rsi_value < 30) or (prices[i] < prices[i - 1] and rsi_value > 70)
        sell_signal = (prices[i] < prices[i - 1] and rsi_value < 30) or (prices[i] > prices[i - 1] and rsi_value > 70)

        # Se realiza una operación si se cumplen las condiciones
        if buy_signal:
            equity.append(equity[i - 1] - prices[i])
            trades.append(1)
        elif sell_signal:
            equity.append(equity[i - 1] + prices[i])
            trades.append(-1)
        else:
            equity.append(equity[i - 1])
            trades.append(0)

    # Se realiza una operación si se cumplen las condiciones
    if buy_signal:
        equity.append(equity[i - 1] - prices[i])
        trades.append(1)
    elif sell_signal:
        equity.append(equity[i - 1] + prices[i])
        trades.append(-1)
    else:
        equity.append(equity[i - 1])
        trades.append(0)

#estrategia breakout

import numpy as np


# Calcular el RSI
def rsi(prices, period):
    delta = prices[-1] - prices[-2]
    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)
    avg_gain = np.mean(gain[-period:])
    avg_loss = np.mean(loss[-period:])
    rs = avg_gain / avg_loss
    return 100 - 100 / (1 + rs)


# Calcular las bandas de Bollinger
def bollinger_bands(prices, period):
    sma = np.mean(prices[-period:])
    std = np.std(prices[-period:])
    upper_band = sma + 2 * std
    lower_band = sma - 2 * std
    return upper_band, lower_band


# Bucle para simular el trading
for i in range(1, len(prices)):
    # Calcular el RSI y las bandas de Bollinger
    rsi_value = rsi(prices, rsi_period)
    upper_band, lower_band = bollinger_bands(prices, bollinger_period)

    # Señales de compra o venta generadas por la estrategia
    buy_signal = (prices[i] > upper_band) and (rsi_value > 50) and (volume[i] > average_volume)
    sell_signal = (prices[i] < lower_band) and (rsi_value < 50) and (volume[i] > average_volume)

    # Se realiza una operación si se cumplen las condiciones
    if buy_signal:
        equity.append(equity[i - 1] - prices[i])
        trades.append(1)
    elif sell_signal:
        equity.append(equity[i - 1] + prices[i])
        trades.append(-1)
    else:
        equity.append(equity[i - 1])
        trades.append(0)


# Función para realizar una operación de compra o venta
def trade(direction):
    global balance
    # Validación de los parámetros de operación
    if stop_loss <= 0 or take_profit <= 0 or balance <= 0:
        print("Error: parámetros de operación inválidos.")
        return

    # Creación del payload para realizar la orden
    payload = {
        "symbol": "BTCUSDT",
        "side": direction,
        "type": "MARKET",
        "quantity": balance * 0.01
    }

    # Envío de la orden a la API
    try:
        response = requests.post("https://api.exchange.com/v1/order", json=payload)
        data = json.loads(response.text)
        if data["status"] == "ERROR":
            print("Error en la orden: " + data["error"])
        else:
            print("Operación realizada con éxito.")
    except requests.exceptions.RequestException as e:
        print("Error en la conexión a la API.")


# Bucle para actualizar el precio del activo de manera recurrente
while True:
    try:
        # Consulta de la información del activo a la API
        response = requests.get("https://api.exchange.com/v1/ticker?symbol=BTCUSDT")
        data = json.loads(response.text)

        # Cálculo de los indicadores
        calc_rsi()
        fibonacci_levels = calc_fibonacci()
        bollinger_bands = calc_bollinger()

        # Toma de decisiones de compra o venta
        try:
            if rsi < 25 and fibonacci_levels[0] and bollinger_bands[0]:
                trade("BUY")
            elif rsi > 75 and fibonacci_levels[1] and bollinger_bands[1]:
                trade("SELL")
        except requests.exceptions.RequestException as e:
            print("Error en la conexión a la API.")
        except Exception as e:
            print("Error desconocido: ", e)

        # Bucle para actualizar el precio del activo de manera recurrente
        while True:
            try:
                # Consulta de la información del activo a la API
                response = requests.get("https://api.exchange.com/v1/ticker?symbol=BTCUSDT")
                data = json.loads(response.text)
            except requests.exceptions.RequestException as e:
                print("Error en la conexión a la API: ", e)
            except Exception as e:
                print("Error desconocido: ", e)

        # Cálculo de los indicadores
        calc_rsi()
        fibonacci_levels = calc_fibonacci()
        bollinger_bands = calc_bollinger()

        # Toma de decisiones de compra o venta
        if rsi < 25 and fibonacci_levels[0] and bollinger_bands[0]:
            trade("BUY")
        elif rsi > 75 and fibonacci_levels[1] and bollinger_bands[1]:
            trade("SELL")
    except requests.exceptions.RequestException as e:
        print("Error en la conexión a la API.")
        break
    except Exception as e:
        print("Error desconocido:", str(e))
        break
# Función para realizar una operación de compra o venta
def trade(direction):
    global balance
    # Validación de los parámetros de operación
    if stop_loss <= 0 or take_profit <= 0 or balance <= 0:
        print("Error: parámetros de operación inválidos.")
        return

    if (direction == "SELL" and balance * (1 - stop_loss) < balance - (balance * 0.01)) or (direction == "BUY" and balance * (1 - stop_loss) < balance + (balance * 0.01)):
        print("Stop loss threshold reached, stopping trading.")
        return

    # Creación del payload para realizar la orden
    payload = {
        "symbol": "BTCUSDT",
        "side": direction,
        "type": "MARKET",
        "quantity": balance * 0.01
    }

    # Envío de la orden a la API
    try:
        response = requests.post("https://api.exchange.com/v1/order", json=payload)
        data = json.loads(response.text)
        if data["status"] == "ERROR":
            print("Error en la orden: " + data["error"])
        else:
            print("Operación realizada con éxito.")
    except requests.exceptions.RequestException as e:
        print("Error en la conexión a la API.")

#VISUALIZACION PERFORMANCE DE ESTRATEGIA

# Lista para almacenar los valores de equidad (balance + ganancias/pérdidas)
equity = [100]

# Lista para almacenar las operaciones realizadas (compra = 1, venta = -1)
trades = []

# Bucle para simular el trading
for i in range(1, len(prices)):
    # Señales de compra o venta generadas por la estrategia
    buy_signal = ...
    sell_signal = ...

    # Se realiza una operación si se cumplen las condiciones
    if buy_signal:
        equity.append(equity[i-1] - prices[i])
        trades.append(1)
    elif sell_signal:
        equity.append(equity[i-1] + prices[i])
        trades.append(-1)
    else:
        equity.append(equity[i-1])
        trades.append(0)

# Gráfico de la performance
plt.plot(equity)
plt.show()

#sistema de gestión de errores (INCOMPLETO)

import logging

# Set up logging
logging.basicConfig(filename='trading_bot.log', level=logging.ERROR)

# Variables para almacenar los valores de RSI y los parámetros de operación
rsi = 0
balance = 100
stop_loss = 0.1
take_profit = 0.3


# Función para calcular el RSI
def calc_rsi():
    global rsi
    try:
        # Cálculo del RSI utilizando la información del activo
        rsi = ...
    except Exception as e:
        logging.error("Error en el cálculo del RSI: %s", e)

# Función para calcular los niveles de fibonacci
def calc_fibonacci():
    try:
        # Cálculo de los niveles de fibonacci utilizando la información del activo
        fibonacci_levels = ...
        return fibonacci_levels
    except Exception as e:
        logging.error("Error en el cálculo de los niveles de fibonacci: %s", e)

# Función para calcular las bandas de bollinger
def calc_bollinger():
    try:
        # Cálculo de las bandas de bollinger utilizando la información del activo
        bollinger_bands = ...
        return bollinger_bands
    except Exception as e:
        logging.error("Error en el cálculo de las bandas de bollinger: %s", e)

# Función para realizar una operación de compra o venta
def trade(direction):
    global balance
    try:
        # Validación de los parámetros de operación
        if stop_loss <= 0 or take_profit <= 0 or balance <= 0:
            raise ValueError("Error: parámetros de operación inválidos.")

        # Creación del payload para realizar la orden
        payload = {
            "symbol": "BTCUSDT",
            "side": direction,
            "type": "MARKET",
            "quantity": balance * 0.01
        }

        # Envío de la orden a la API
        response = requests.post("https://api.exchange.com/v1/order", json=payload)
        data = json.loads(response.text)
        if data["status"] == "ERROR":
            raise ValueError("Error en la orden: " + data["error"])
        else:
            print("Operación realizada con éxito.")
    except ValueError as e:
        logging.error(e)
    except requests.exceptions.RequestException as e:
        logging.error("Error en la conexión a la API: %s", e)
    except Exception as e:
        logging.error("Error desconocido")

