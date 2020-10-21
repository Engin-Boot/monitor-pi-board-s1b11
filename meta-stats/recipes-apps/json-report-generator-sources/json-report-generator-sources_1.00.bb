SUMMARY = "Read package name and package version from manifest file and generate a JSON report"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "\
file://COPYING;md5=0835ade698e0bcf8506ecda2f7b4f302 \
"

SRC_URI = "\
file://COPYING \
file://json-report-generator.py \
file://package_json_object_creator.py \
file://package_json_report_writer.py \
"

S = "${WORKDIR}"

do_compile() {
  python3 json-report-generator.py -i ${DEPLOY_DIR_IMAGE}/core-image-sato-${MACHINE}.manifest -o ${DEPLOY_DIR}/
}

do_install() {
  install -d "${D}${bindir}"
  install -m 0755 json-report-generator.py "${D}${bindir}"
}
