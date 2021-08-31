const composer = require('@ibm-functions/composer')

module.exports = composer.sequence(
    composer.action('ListFiles', { limits: { timeout: 300000 } }),
    composer.map(
        composer.action('TransformData', { limits: { timeout: 300000 } })
    ),
    composer.action('AggregateData', { limits: { timeout: 300000 } }),
    composer.action('CleanUp', { limits: { timeout: 300000 } })
)