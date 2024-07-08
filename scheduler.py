import asyncio
import logging

from scheduler.base import setup_scheduler, schedule_tasks


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    scheduler = await setup_scheduler()
    schedule_tasks(scheduler)
    scheduler.start()
    while True:
        await asyncio.sleep(100)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info('Exited')
