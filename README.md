# K3S Headscale Route Manager

Fancy name for a simple tool that makes sure headscale routes are up.

## How to use

This container needs 2 environment variables to run:
- `API_URL`: The URL of the headscale API.
- `API_KEY`: The API key for authenticating with the headscale API.

Optionally, you can set `CHECK_INTERVAL` to define how often (in seconds) the tool checks the routes. The default is 60 seconds.

## Goal

When k3s nodes restart or lose connectivity, headscale routes can become down. This tool ensures that routes are enabled.

## Dependencies

This project only need access to the headscale API.

## Architecture

This project uses a loop to periodically check the status of headscale routes and re-enable them if they are down.

## License  

This project is licensed under the **MIT License**.