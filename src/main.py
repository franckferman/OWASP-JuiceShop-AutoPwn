#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main entry point for OWASP Juice Shop AutoPwn.

This script automates Juice Shop challenges using Selenium and Requests.

Author: franckferman
Date: 2025-03-07
Version: 1.0.0
"""

from time import sleep

from challenges.juiceshop_challenges import (
    admin_registration, admin_section, bonus_payload, bully_chatbot, captcha_bypass,
    confidential_document, csrf, database_schema, deluxe_fraud, dom_xss, easter_egg,
    error_handling, exposed_metrics, forged_feedback, forged_review, gdrp_data_erasure,
    login_admin, login_amy, login_bender, login_jim, login_mc_safesearch,
    manipulate_basket, meta_geo_stalking, missing_encoding, outdated_allowlist,
    password_strength, payback_time, privacy_policy, reflected_xss, repetitive_registration,
    reset_benders_password, scoreboard, security_policy, deprecated_interface,
    log_off, view_basket, visual_geo_stalking, vulnerable_library, zero_stars
)

from parser import setup_arg_parser
from selenium_utils.selenium_setup import setup_webdriver
from selenium_utils.selenium_utils import open_homepage_wait_for_juiceshop_logo_and_dismiss_welcomebanner
from utils.validations import add_port, juice_shop_validation, url_validation


def main():
    parser = setup_arg_parser()
    args = parser.parse_args()

    if args.ip is not None and args.domain is None:
        url_address = url_validation(args.ip)
    elif args.domain is not None and args.ip is None:
        url_address = url_validation(args.domain)

    if args.port is not None:
        url_address = add_port(url_address, args.port)

    if not juice_shop_validation(url_address):
        print("The Juice Shop instance is unavailable.")
        return

    try:
        driver, wait = setup_webdriver(args.browser, args.wait_time)

        open_homepage_wait_for_juiceshop_logo_and_dismiss_welcomebanner(driver, url_address, wait)
        sleep(1)
        scoreboard(driver, wait, url_address)
        sleep(1)
        dom_xss(driver, wait, url_address)
        sleep(1)
        bonus_payload(driver, wait, url_address)
        sleep(1)
        confidential_document(driver, wait, url_address)
        sleep(1)
        error_handling(driver, wait, url_address)
        sleep(1)
        exposed_metrics(driver, wait, url_address)
        sleep(1)
        missing_encoding(driver, wait, url_address)
        sleep(1)
        outdated_allowlist(driver, wait, url_address)
        sleep(1)
        privacy_policy(driver, wait, url_address)
        sleep(1)
        repetitive_registration(driver, wait, url_address)
        sleep(1)
        login_admin(driver, wait, url_address)
        sleep(1)
        admin_section(driver, wait, url_address)
        sleep(1)
        log_off(driver, wait, url_address)
        sleep(1)
        login_mc_safesearch(driver, wait, url_address)
        sleep(1)
        password_strength(driver, wait, url_address)
        sleep(1)
        bully_chatbot(driver, wait, url_address)
        sleep(1)
        zero_stars(url_address)
        sleep(1)
        view_basket(driver, wait, url_address)
        sleep(1)
        deprecated_interface(driver, wait, url_address)
        sleep(1)
        easter_egg(driver, wait, url_address)
        sleep(1)
        security_policy(driver, wait, url_address)
        sleep(1)
        vulnerable_library(driver, wait, url_address)
        sleep(1)
        reflected_xss(driver, wait, url_address)
        sleep(1)
        open_homepage_and_wait_for_juiceshop_logo
        sleep(1)
        log_off(driver, wait, url_address)
        sleep(1)
        meta_geo_stalking(driver, wait, url_address)
        sleep(1)
        visual_geo_stalking(driver, wait, url_address)
        sleep(1)
        admin_registration(driver, wait, url_address, "admin", "admin", "admin")
        sleep(1)
        password_strength(driver, wait, url_address)
        sleep(1)
        manipulate_basket()
        sleep(1)
        captcha_bypass(driver, wait, url_address)
        sleep(1)
        zero_stars(url_address)
        sleep(1)
        forged_feedback(url_address)
        sleep(1)
        csrf(url_address)
        sleep(1)
        database_schema(driver, wait, url_address)
        sleep(1)
        deluxe_fraud(url_address)
        sleep(1)
        forged_review(url_address)
        sleep(1)
        log_off(driver, wait, url_address)
        sleep(1)
        gdrp_data_erasure(driver, wait, url_address)
        sleep(1)
        log_off(driver, wait, url_address)
        sleep(1)
        login_amy(driver, wait, url_address)
        sleep(1)
        login_bender(driver, wait, url_address)
        sleep(1)
        login_jim(driver, wait, url_address)
        sleep(1)
        reset_benders_password(driver, wait, url_address)
        payback_time(url_address)

    except Exception as e:
        print("An error has occurred : ", str(e))

    finally:
        if driver is not None:
            input("\nPress Enter to quit...")
            driver.quit()


if __name__ == "__main__":
    main()
