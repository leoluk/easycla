// Copyright The Linux Foundation and each contributor to CommunityBridge.
// SPDX-License-Identifier: MIT

package utils

import "strings"

// TrimRemoveTrailingComma trims the whitespace on the specified string and removes the trailing comma
func TrimRemoveTrailingComma(input string) string {
	if input == "" {
		return input
	}

	s := strings.TrimSpace(input)
	return strings.TrimSuffix(s, ",")
}
