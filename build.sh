#!/usr/bin/env bash
# 运行单元测试和覆盖率测试，用于软工平台每次push后自动测试

coverage run --source='.' manage.py test
coverage html -d Coverage_Python
