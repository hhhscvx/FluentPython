from keyword import kwlist

from curio import run, TaskGroup, socket


MAX_KEYWORD_LEN = 4


async def probe(domain: str) -> tuple[str, bool]:
    try:
        await socket.getaddrinfo(host=domain, port=None)
    except socket.gaierror:
        return domain, False
    return domain, True


async def main() -> None:
    names = (kw for kw in kwlist if len(kw) <= MAX_KEYWORD_LEN)
    domains = (f"{domain}.dev" for domain in names)
    async with TaskGroup() as group:
        for domain in domains:
            await group.spawn(probe, domain)  # запускать эту корутину, и сохраняет результаты в group
        async for task in group:
            domain, found = task.result
            mark = '+' if found else ' '
            print(f'{mark} {domain}')

if __name__ == "__main__":
    run(main())
