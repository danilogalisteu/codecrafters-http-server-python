from lib import curio


async def client_connected_task(client: curio.io.Socket, addr: tuple[str, int]) -> None:
    status = "HTTP/1.1 200 OK"
    headers = ""
    body = ""

    response = "\r\n".join([status, headers, body])

    await client.sendall(response.encode())


def main():
    curio.run(
        curio.tcp_server("localhost", 4221, client_connected_task, reuse_port=True)
    )


if __name__ == "__main__":
    main()
