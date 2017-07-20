# this script is for building the app for android through Linux #
#$ debug $1
#$ passwd $2
echo 'Copying androidmanifest template...'
cp AndroidManifest.tmpl.xml .buildozer/android/platform/build/dists/emojicountdown/templates
echo 'Finished copying the manifest template.'
echo 'Build process beginning...'

openssl aes-256-ecb -d -in emoji.keystore.aes-256-ecb -out emoji.keystore

export P4A_RELEASE_KEYSTORE=~/EmojiMovieCountdown/emoji.keystore
export P4A_RELEASE_KEYALIAS=emoji
export P4A_RELEASE_KEYSTORE_PASSWD=$2
export P4A_RELEASE_KEYALIAS_PASSWD=$2

buildozer android $1

rm emoji.keystore
