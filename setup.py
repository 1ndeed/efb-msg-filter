from setuptools import setup, find_packages

setup(
    name='efb-msg-filter',
    packages=find_packages(),
    version='0.1.0',
    description='Advanced Features For EQS, EWCS, EWS.',
    author='Riley Soong',
    auther_email='aurman@qq.com',
    url='https://github.com/iaurman/efb-msg-filter',
    include_package_data=True,
    install_requires=[
        "ehforwarderbot"
    ],
    entry_points={
        "ehforwarderbot.middleware": "rileysoong.msg_filter = efb_msg_filter:FilterMiddleware"
    }
    )
