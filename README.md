# Vehicle Simulator

This project simulates some of the commands like accelerating, braking, and steering for a network based vehicle simulator. The communication occurs via socket programming in Python, with commands serialized in JSON format.

## How to run the program

1. Clone the project

```bash
git clone https://github.com/yesar-codes/Message_Protocol.git
```

2. Install Python (if not installed)

Python 3.10 or later is recommended.

3. Go to Terminal and run the command

```bash
cd src
```

4. Run the Server

```bash
python server.py
```

5. Run the Client in another terminal

```bash
python client.py
```

## Configuration

Commands are given through commands.json file

```json
{
  "commands": [
    { "command": "accelerate", "value": 100 },
    { "command": "brake", "value": 50 },
    { "command": "steer", "direction": "left" },
    { "command": "steer", "direction": "right" }
  ]
}
```

More commands can be added if want to simulate more

## How it works

1. The Client reads the commands from the commands.json and sends it to the server.
2. The Server processes the commands and updates the vehicle state accordingly
3. The updated state is send as a response

## Commands

1. Accelerate - increases the vehicle's speed.
2. Brake - decrease the vehicle's speed
3. Steer - changes the vehicle direction to left or right from initial straight state
