#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:Lijiacai
Email:1050518702@qq.com
===========================================
CopyRight@JackLee.com
===========================================
"""

import os
import re
import sys
import json
import graphene
from common.view import BaseApi
from resource.lijiacai.utils import utils
from sql import *
from sql.aggregate import *
from sql.functions import *
from sql.conditionals import *


class query_user(utils.Business, BaseApi, utils.MySQLCrud):
    name = "query_user"
    description = "用户查询(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        print(result)
        return {"ret": result}


class query_role(utils.Business, BaseApi, utils.MySQLCrud):
    name = "query_role"
    description = "角色查询(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class query_organization(utils.Business, BaseApi, utils.MySQLCrud):
    name = "query_organization"
    description = "组织机构查询(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class query_city(utils.Business, BaseApi, utils.MySQLCrud):
    name = "query_city"
    description = "城市查询(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class query_function(utils.Business, BaseApi, utils.MySQLCrud):
    name = "query_function"
    description = "功能配置(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class query_Role_function(utils.Business, BaseApi, utils.MySQLCrud):
    name = "query_Role_function"
    description = "角色功能(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class query_business_group(utils.Business, BaseApi, utils.MySQLCrud):
    name = "query_business_group"
    description = "业务组(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class query_business(utils.Business, BaseApi, utils.MySQLCrud):
    name = "query_business"
    description = "开发业务(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class query_business_function(utils.Business, BaseApi, utils.MySQLCrud):
    name = "query_business_function"
    description = "附加功能(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class worksheet_manage_ing(utils.Business, BaseApi, utils.MySQLCrud):
    name = "worksheet_manage_ing"
    description = "工单信息（处理中(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class worksheet_manage_ed(utils.Business, BaseApi, utils.MySQLCrud):
    name = "worksheet_manage_ed"
    description = "工单信息（已处理）(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class worksheet_record_six(utils.Business, BaseApi, utils.MySQLCrud):
    name = "worksheet_record_six"
    description = "工单动态最新前6条记录(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class base_stations(utils.Business, BaseApi, utils.MySQLCrud):
    name = "base_stations"
    description = "基础站点信息(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class base_vehicle_view(utils.Business, BaseApi, utils.MySQLCrud):
    name = "base_vehicle_view"
    description = "站点下车辆信息(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


###########################
class create_user(utils.Business, BaseApi, utils.MySQLCrud):
    name = "create_user"
    description = "新建用户(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class update_user(utils.Business, BaseApi, utils.MySQLCrud):
    name = "update_user"
    description = "更新用户(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class create_role(utils.Business, BaseApi, utils.MySQLCrud):
    name = "create_role"
    description = "创建角色(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class update_role(utils.Business, BaseApi, utils.MySQLCrud):
    name = "update_role"
    description = "更新角色(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class delete_role(utils.Business, BaseApi, utils.MySQLCrud):
    name = "delete_role"
    description = "删除角色(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class create_organization(utils.Business, BaseApi, utils.MySQLCrud):
    name = "create_organization"
    description = "新建组织机构(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class update_organization(utils.Business, BaseApi, utils.MySQLCrud):
    name = "update_organization"
    description = "更新组织结构(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class create_city(utils.Business, BaseApi, utils.MySQLCrud):
    name = "create_city"
    description = "新建城市(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class update_city(utils.Business, BaseApi, utils.MySQLCrud):
    name = "update_city"
    description = "更新城市(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class update_station(utils.Business, BaseApi, utils.MySQLCrud):
    name = "update_station"
    description = "更新站点(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class create_function(utils.Business, BaseApi, utils.MySQLCrud):
    name = "create_function"
    description = "新建功能配置(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class update_function(utils.Business, BaseApi, utils.MySQLCrud):
    name = "update_function"
    description = "更新功能配置(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class create_role_function(utils.Business, BaseApi, utils.MySQLCrud):
    name = "create_role_function"
    description = "角色关联(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class create_business_group(utils.Business, BaseApi, utils.MySQLCrud):
    name = "create_business_group"
    description = "创建业务组(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class update_business_group(utils.Business, BaseApi, utils.MySQLCrud):
    name = "update_business_group"
    description = "新建用户(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class delete_business_group(utils.Business, BaseApi, utils.MySQLCrud):
    name = "delete_business_group"
    description = "删除业务组(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class create_group_position(utils.Business, BaseApi, utils.MySQLCrud):
    name = "create_group_position"
    description = "职位关联(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class create_business(utils.Business, BaseApi, utils.MySQLCrud):
    name = "create_business"
    description = "开发业务表(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class create_business_function(utils.Business, BaseApi, utils.MySQLCrud):
    name = "create_business_function"
    description = "附加功能(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class create_business_config(utils.Business, BaseApi, utils.MySQLCrud):
    name = "create_business_config"
    description = "业务关联配置(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class gen_worksheet(utils.Business, BaseApi, utils.MySQLCrud):
    name = "gen_worksheet"
    description = "生成工单 发起普调(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class submission_worksheet(utils.Business, BaseApi, utils.MySQLCrud):
    name = "create_user"
    description = "(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class pickup_worksheet(utils.Business, BaseApi, utils.MySQLCrud):
    name = "create_user"
    description = "(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class report_worksheet(utils.Business, BaseApi, utils.MySQLCrud):
    name = "report_worksheet"
    description = "(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class return_worksheet(utils.Business, BaseApi, utils.MySQLCrud):
    name = "return_worksheet"
    description = "(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class return_sub_worksheet(utils.Business, BaseApi, utils.MySQLCrud):
    name = "return_sub_worksheet"
    description = "(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class confirm_worksheet(utils.Business, BaseApi, utils.MySQLCrud):
    name = "confirm_worksheet"
    description = "(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class abnormal_worksheet(utils.Business, BaseApi, utils.MySQLCrud):
    name = "create_user"
    description = "(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}


class lock_vehicle(utils.Business, BaseApi, utils.MySQLCrud):
    name = "create_user"
    description = "(done)"

    def validate_privilege(self, token_info, **kwargs):
        pass

    def deal(self, token_info, prilivege_info, **kwargs):
        self.validate_graphql_api(name=self.name)
        return self.run()

    def dealer(self):
        # todo:参数处理，加数据权限参数
        self.backend_params["json"] = self.service_args
        response = self.backend_service()
        result = json.dumps(response.json())
        return {"ret": result}
